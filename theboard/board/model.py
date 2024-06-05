from typing import Optional, List

from autogen import ConversableAgent


class BoardMember:
    _name: str
    _description: str

    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description

    def name(self) -> str: return self._name

    def description(self) -> str: return self._description

    def agent(self) -> ConversableAgent:
        pass


class BoardRoom:
    _name: str
    _description: str
    _board_members: List[BoardMember]

    def __init__(self, name: str, description: str, board_members: List[BoardMember]):
        self._name = name
        self._description = description
        self._board_members = board_members

    def name(self) -> str: return self._name

    def description(self) -> str: return self._description

    def board_members(self) -> List[BoardMember]: return self._board_members


class TheBoard:
    _board_rooms: List[BoardRoom]

    def __init__(self, board_rooms: List[BoardRoom]):
        self._board_rooms = board_rooms

    def board_rooms(self) -> List[BoardRoom]:
        return self._board_rooms

    def room_by_name(self, room_name: str) -> Optional[BoardRoom]:
        for room in self._board_rooms:
            if room.name() == room_name:
                return room

        return None

    def member_by_name(self, member_name: str) -> Optional[BoardMember]:
        for room in self._board_rooms:
            for member in room.board_members():
                if member.name() == member_name:
                    return member

        return None
