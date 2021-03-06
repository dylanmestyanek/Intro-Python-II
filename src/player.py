# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = {}

    def __str__(self):
        return f'Player: {self.name}\n{self.current_room}'

    def move_player(self, direction):
        destination = getattr(self.current_room, f'{direction}_to')
        if destination != None:
            self.current_room = destination
            print(f'\n========================\n>>> CURRENT LOCATION <<<\n========================\n{self}')
        else:
            print('\n ———————————————————————————————————————————————————\n|  Woops, looks like you can\'t head that direction. |\n|           Try taking a different path!            |\n ———————————————————————————————————————————————————\n                         ||\n                         ||\n                         ||\n') 
    
    def pickup_item(self, current_room, cmd, action):
        if len(cmd) < 2:
            return print(f'\nWoops! Invalid command. When attempting to {action} an item type: [{action[0]} *item name*]\n')

        item = cmd[1]

        if item in current_room.items:
            self.items[item] = current_room.items[item]
            print(current_room.items[item].take_item())
            del current_room.items[item]
        else:
            print('\n\n► ► ►  Looks like that item isn\'t in this room! ◄ ◄ ◄ ')

    def drop_item(self, current_room, cmd, action):
        if len(cmd) < 2:
            return print(f'\nWoops! Invalid command. When attempting to {action} an item type: [{action[0]} *item name*]\n')

        item = cmd[1]
        if item in self.items:
            current_room.items[item] = self.items[item]
            print(current_room.items[item].drop_item())
            del self.items[item]
        else:
            print('\n\n► ► ►  Looks like that item isn\'t in your inventory! ◄ ◄ ◄ ')

    def view_inventory(self):
        inventory = f'\n========================\n>>>  YOUR INVENTORY  <<<\n========================\n'
        if self.items:
            for i in self.items:
                inventory += f' [{i}] '
        else:
            inventory += 'Your inventory is empty!'
        return inventory

    def view_location(self):
        return f'\n========================\n>>> CURRENT LOCATION <<<\n========================\n{self}'
