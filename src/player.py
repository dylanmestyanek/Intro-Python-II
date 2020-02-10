# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def __str__(self):
        return f'Current Room: {self.current_room}'

    def __repr__(self):
        return f'Player({repr(self.current_room)})'


