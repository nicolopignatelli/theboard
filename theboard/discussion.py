import logging
from dataclasses import dataclass
from functools import reduce
from typing import List, Dict, TypeAlias

from autogen import ConversableAgent, GroupChat, GroupChatManager

from theboard import pubsub
from theboard.config import LLM_CONFIG
from theboard.board.model import TheBoard, BoardMember
import theboard.messages as messages

logger = logging.getLogger(__name__)

IS_RELEVANT = "RELEVANT"
IS_NOT_RELEVANT = "NOT RELEVANT"
IS_RELEVANT_PROMPT_TEMPLATE = (f"Answer the following question with \"{IS_RELEVANT}\" or \"{IS_NOT_RELEVANT}\" only.\n"
                               "Question: Is your knowledge relevant enough to contribute to a conversation on the "
                               "following matter?\n{matter}")


def is_relevant(member: BoardMember, matter: str) -> bool:
    is_relevant_reply = member.agent().generate_reply(
        messages=[{"content": IS_RELEVANT_PROMPT_TEMPLATE.format(matter=matter), "role": "user"}])
    print(f"{member.name()} said that their knowledge {is_relevant_reply}.")
    return is_relevant_reply == IS_RELEVANT


def user() -> ConversableAgent:
    return ConversableAgent(
        "human_proxy",
        llm_config=False,
        human_input_mode="NEVER",
    )


def chat_with_board_members(board_members: List[BoardMember], matter: str, discussion_forum_id: str):
    how_many_board_members = len(board_members)
    if how_many_board_members >= 2:
        speaker_selection_method = "auto"
        if how_many_board_members == 2:
            speaker_selection_method = "round_robin"

        group_chat = GroupChat(agents=list(map(lambda dg: dg.agent(), board_members)), messages=[],
                               max_round=3 * how_many_board_members, send_introductions=True, speaker_selection_method=speaker_selection_method)
        group_chat_manager = GroupChatManager(groupchat=group_chat, llm_config=LLM_CONFIG)
        result = user().initiate_chat(group_chat_manager, message=matter, summary_method="reflection_with_llm")
        return result.summary

    if how_many_board_members == 1:
        single_board_member = board_members[0]
        member_name = single_board_member.name()
        member_reply = single_board_member.agent().generate_reply([{"content": matter, "role": "user"}])
        pubsub.publish(discussion_forum_id, messages.MemberReplied(member_name=single_board_member.name(), reply=member_reply))
        logger.info(f"{single_board_member.name()} replied")
        return member_name + "\n" + member_reply


class MembersSelectionMethod:
    def select_members(self, matter, discussion_forum_id: str) -> List[BoardMember]:
        pass


@dataclass
class SingleRoom(MembersSelectionMethod):
    the_board: TheBoard
    room_name: str
    relevant_members_only: bool = True

    def select_members(self, matter: str, discussion_forum_id: str) -> List[BoardMember]:
        logger.info("Using SingleRoom members selection method")

        room = self.the_board.room_by_name(self.room_name)

        if room is None:
            ex = Exception("Room not found: " + self.room_name)
            logger.error(ex)
            raise ex

        relevant_members: List[BoardMember] = []

        for member in room.board_members():
            if self.relevant_members_only and is_relevant(member, matter):
                relevant_members.append(member)
                pubsub.publish(discussion_forum_id, message=messages.MemberWasSelected(member_name=member.name()))
            else:
                pubsub.publish(discussion_forum_id, message=messages.MemberWasNotSelected(member_name=member.name()))

        return relevant_members

    def __str__(self):
        return "SingleRoom"


@dataclass
class SelectedBoardMembers(MembersSelectionMethod):
    the_board: TheBoard
    member_names: List[str]

    def select_members(self, matter: str, discussion_forum_id: str) -> List[BoardMember]:
        logger.info("Using SelectedBoardMembers members selection method")

        selected_members: List[BoardMember] = []
        for member_name in self.member_names:
            board_member = self.the_board.member_by_name(member_name)
            if board_member is None:
                ex = Exception("Board member not found: " + member_name)
                logger.error(ex)
                raise ex

            selected_members.append(board_member)
            pubsub.publish(discussion_forum_id, message=messages.MemberWasNotSelected(member_name=board_member.name()))

        return selected_members


@dataclass
class CompleteBoard(MembersSelectionMethod):
    the_board: TheBoard
    relevant_members_only: bool = True

    def select_members(self, matter: str, discussion_forum_id: str) -> List[BoardMember]:
        logger.info("Using CompleteBoard members selection method")

        relevant_members: List[BoardMember] = []

        for room in self.the_board.board_rooms():
            for member in room.board_members():
                if self.relevant_members_only and is_relevant(member, matter):
                    relevant_members.append(member)
                    pubsub.publish(discussion_forum_id, message=messages.MemberWasSelected(member_name=member.name()))
                else:
                    pubsub.publish(discussion_forum_id, message=messages.MemberWasNotSelected(member_name=member.name()))

        return relevant_members


MemberName: TypeAlias = str
MemberRelevancyScore: TypeAlias = float


@dataclass
class SelectTheMostRelevant(MembersSelectionMethod):
    the_board: TheBoard
    max_members: int = 1
    max_members_considered_in_a_room: int = 3

    def select_members(self, matter: str, discussion_forum_id: str) -> List[BoardMember]:
        logger.info("Using SelectTheMostRelevant members selection method")

        list_of_rooms = reduce(
            lambda list_str, r_str: f"{list_str}\n{r_str}",
            map(lambda r: f"{r.name()} - {r.description()}", self.the_board.board_rooms())
        )

        room_ranker = ConversableAgent(
            "Room_Ranker",
            system_message="Your task is to rank the rooms from the following list. To correctly rank the rooms, you must take the following information and ranking criteria in account:\n"
                           "- The goal is to rank the rooms from the highest to the lowest probability of finding the best expert to discuss the matter that the user will submit.\n"
                           "- Typically, each room represent a pool of experts in a specific discipline. There are exceptions, so always look at the desccription of the room.\n"
                           "- Always reply with a new line separated list of the room names and nothing else."
                           f"List of rooms:\n{list_of_rooms}",
            llm_config=LLM_CONFIG,
            human_input_mode="NEVER",
        )

        room_ranker_output = (room_ranker
                              .generate_reply([{"content": "Matter:\n" + matter, "role": "user"}])
                              .strip("\n")
                              .split("\n"))

        pubsub.publish(discussion_forum_id, message=messages.RoomRankerOutput(ranked_rooms=room_ranker_output))

        logger.info("Room ranker output: " + str(room_ranker_output))

        selected_members: List[BoardMember] = []
        members_to_score: Dict[MemberName, MemberRelevancyScore] = {}

        for room_name in room_ranker_output:
            room = self.the_board.room_by_name(room_name)
            if room is None:
                ex = Exception("Room not found: " + room_name)
                logger.error(ex)
                raise ex

            list_of_room_members = reduce(
                lambda list_str, m_str: f"{list_str}\n{m_str}",
                map(lambda m: f"{m.name()} - {m.description()}", room.board_members())
            )

            member_ranker = ConversableAgent(
                "Member_Ranker",
                system_message=f"Your task is to select the {self.max_members_considered_in_a_room} most relevant entities from the following list and rank them. To correctly rank the entities, you must take the following information and ranking criteria in account:\n"
                               "- The goal is to rank the entities from the highest to the lowest relevancy of their knowledge for the matter that the user will submit.\n"
                               "- You must also assign a ranking score to each entities in the [0, 1] interval, where 1 is the maximum relevancy score.\n"
                               "- Always reply with a new line separated list of items. Each item follows the format <entity name (only the name!)>;<relevancy score>. E.g. Entity1;0.68\\nEntity2;0.2\n"
                               f"List of entities:\n{list_of_room_members}",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

            member_ranker_output = (member_ranker
                                    .generate_reply([{"content": "Matter:\n" + matter, "role": "user"}])
                                    .strip("\n")
                                    .split("\n"))

            pubsub.publish(discussion_forum_id, message=messages.MemberRankerOutput(room_name=room_name, ranked_members=member_ranker_output))

            logger.info(f"Member ranker output for room {room_name}:" + str(member_ranker_output))

            room_ranking: Dict[MemberName, MemberRelevancyScore] = {}
            for member_ranker_row in member_ranker_output:
                (member_name, member_score) = member_ranker_row.split(";")
                room_ranking[member_name] = max(float(members_to_score.get(member_name, 0)), float(member_score))

            members_to_score.update(room_ranking)

        ranked_members_to_score = dict(sorted(members_to_score.items(), key=lambda item: item[1], reverse=True))

        logger.info("Ranked members->scores: " + str(ranked_members_to_score))

        for member_name in list(ranked_members_to_score.keys())[:self.max_members]:
            board_member = self.the_board.member_by_name(member_name)
            if board_member is None:
                ex = Exception("Board member not found: " + member_name)
                logger.error(ex)
                raise ex

            selected_members.append(board_member)

            pubsub.publish(discussion_forum_id, message=messages.MemberWasSelected(member_name=board_member.name()))
            logger.info(f"{board_member.name()} was selected for the discussion forum")

        return selected_members


@dataclass
class DiscussionForum:
    _discussion_forum_id: str
    _members_selection_method: MembersSelectionMethod
    _matter: str

    def discuss(self):
        selected_board_members = self._members_selection_method.select_members(matter=self._matter, discussion_forum_id=self._discussion_forum_id)
        return chat_with_board_members(selected_board_members, self._matter, self._discussion_forum_id)
