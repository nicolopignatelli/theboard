from typing import List

from theboard.pubsub import Message


class RoomRankerOutput(Message):
    ranked_rooms: List[str]


class MemberRankerOutput(Message):
    room_name: str
    ranked_members: List[str]


class MemberWasSelected(Message):
    member_name: str


class MemberWasNotSelected(Message):
    member_name: str


class DiscussionForumStarted(Message):
    discussion_forum_id: str
    member_selection_method_name: str


class MemberReplied(Message):
    member_name: str
    reply: str
