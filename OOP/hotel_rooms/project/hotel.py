from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room_take = next(filter(lambda x: x.number == room_number, self.rooms))

        except StopIteration:
            return

        result = room_take.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            room_free = next(filter(lambda x: x.number == room_number, self.rooms))

        except StopIteration:
            return
        people = room_free.guests
        result = room_free.free_room()

        if not result:
            self.guests -= people

    def status(self):
        result = f'Hotel {self.name} has {self.guests} total guests\n'
        result += f'Free rooms: {", ".join(str(r.number) for r in self.rooms if not r.is_taken)}\n'
        result += f'Taken rooms: {", ".join(str(r.number) for r in self.rooms if r.is_taken)}'
        return result

