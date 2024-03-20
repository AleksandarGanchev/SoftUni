from typing import List

from project import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        self.guests, free_rooms, taken_rooms = 0, [], []
        for x in self.rooms:
            if x.is_taken:
                taken_rooms.append(str(x.number))
                self.guests += x.guests
            else:
                free_rooms.append(str(x.number))
        output = [f"Hotel {self.name} has {self.guests} total guests",
                  f"Free rooms: {', '.join(free_rooms)}",
                  f"Taken rooms: {', '.join(taken_rooms)}"]

        return "\n".join(output)

