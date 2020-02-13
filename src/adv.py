from room import Room
from player import Player
from items_inventory import items

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", {'necklace': items['necklace'], 'coins': items['coins'], 'flowerpot': items['flowerpot']}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", {'rope': items['rope'], 'pickaxe': items['pickaxe'], 'shoe': items['shoe']}),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", {'bones': items['bones'], 'shovel': items['shovel'], 'gems': items['gems']}),

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

player = Player('Big Boy', room['outside'])

print('\nWelcome to your adventure!\nWhatever you do, be careful.. and don\'t get lost!')
print(f'\n========================\n>>> CURRENT LOCATION <<<\n========================\n{player}')
while True:
    cmd = input("\n===> Where are you headed next?\n===> [n] North - [e] East - [s] South - [w] West - [i] Inventory - [p] Pick Up Item - [l] Location - [q] Quit\n").split(" ")

    if cmd[0] in ['n', 's', 'e', 'w']:
        player.move_player(cmd[0])
    elif cmd[0] == 'p':
        player.pickup_item(player.current_room, cmd)
    elif cmd[0] == 'i':
        print(player.view_inventory())
    elif cmd[0] == 'l':
        print(player.view_location())
    elif cmd[0] == 'q':
        print("\nSafe travels!\nReturn when you're strong enough to continue your adventure!\n")
        exit()
    else:
        print('\n>>>>> That is not a valid input. Try again! <<<<<')


