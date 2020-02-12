from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["coins", "necklace", "flowerpot"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["rope", "pickaxe", "shoe"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["bones", "shovel", "gems"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

commands = ['n', 's', 'e', 'w', 'q', 'take', 'get']

def move_player(new_destination):
    if new_destination != None:
        player_one.current_room = new_destination
    else:
        print('\n ———————————————————————————————————————————————————\n|  Woops, looks like you can\'t head that direction. |\n|           Try taking a different path!            |\n ———————————————————————————————————————————————————\n                         ||\n                         ||\n                         ||\n')
        
# Make a new player object that is currently in the 'outside' room.
player_one = Player('Big Daddy', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
print('\nWelcome to your adventure!\nWhatever you do, be careful.. and don\'t get lost!')
while True:
    print(f'\n========================\n>>> CURRENT LOCATION <<<\n========================\n{player_one}')
    player_cmd = input("\n===> Where are you headed next?\n===> [n] North - [e] East - [s] South - [w] West - [q] Quit\n")

    player_cmd = player_cmd.split(" ")

    if player_cmd[0] in commands:
        if player_cmd[0] == 'n':
            move_player(player_one.current_room.n_to)
        elif player_cmd[0] == 'e':
            move_player(player_one.current_room.e_to)
        elif player_cmd[0] == 's':
            move_player(player_one.current_room.s_to)
        elif player_cmd[0] == 'w':
            move_player(player_one.current_room.w_to)
        elif player_cmd[0] == 'take' or player_cmd[0] == 'get' and len(player_cmd) == 2:
            if player_cmd[1] in player_one.current_room.items:
                player_one.items.append(player_cmd[1])
                player_one.current_room.items.remove(player_cmd[1])
                
            else:
                print('\n\n► ► ►  Looks like that item isn\'t in this room! ◄ ◄ ◄ ')
        elif player_cmd[0] == 'q':
            print("\nSafe travels!\nReturn when you're strong enough to continue your adventure!\n")
            exit()
    else:
        print('\n>>>>> That is not a valid input. Try again! <<<<<')


