from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

def move_character(new_destination):
    if new_destination != None:
        player_one.current_room = new_destination
    else:
        print('\n ———————————————————————————————————————————————————\n|  Woops, looks like you can\'t head that direction. |\n|           Try taking a different path!            |\n ———————————————————————————————————————————————————\n                         ||\n                         ||\n                         ||\n')
        
# Make a new player object that is currently in the 'outside' room.
player_one = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
print('\nWelcome to your adventure!\nWhatever you do, be careful.. and don\'t get lost!\n')
while True:
    print(f'=== Current Location ===\n{player_one}')
    # print(f'\n{room[player_one.current_room]}')
    # print(f'WHAT I NEED {room[player_one.current_room].n_to}')
    player_cmd = input("\nWhere are you headed next?\n[1] North - [2] East - [3] South - [4] West - [q] Quit\n")

    if player_cmd == '1':
        move_character(player_one.current_room.n_to)
    elif player_cmd == '2':
        move_character(player_one.current_room.e_to)
    elif player_cmd == '3':
        move_character(player_one.current_room.s_to)
    elif player_cmd == '4':
        move_character(player_one.current_room.w_to)
    elif player_cmd == 'q':
        print("\nSafe travels!\nReturn when your strong enough to continue your adventure!\n")
        exit()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


