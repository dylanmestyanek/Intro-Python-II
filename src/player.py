# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f'Player: {self.name}\n{self.current_room}'

    def move_player(self, new_destination):
        if new_destination != None:
            self.current_room = new_destination
            print(f'\n========================\n>>> CURRENT LOCATION <<<\n========================\n{self}')
        else:
            print('\n ———————————————————————————————————————————————————\n|  Woops, looks like you can\'t head that direction. |\n|           Try taking a different path!            |\n ———————————————————————————————————————————————————\n                         ||\n                         ||\n                         ||\n') 


