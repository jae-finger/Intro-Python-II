from room import Room
from player import Player

# # Declare all the rooms
# outside = Room("Outside Cave Entrance",
#                "North of you, the cave mount beckons", n_to='foyer')

# foyer = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.",
#              s_to='outside', n_to='overlook', e_to='narrow')

# overlook = Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", s_to='foyer')

# narrow = Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.",
#               w_to='foyer', n_to='treasure')

# treasure = Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", s_to='narrow')
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons."),

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

# Make a new player object that is currently in the 'outside' room.
player1 = Player(name='Jon', player_room=room['outside'])

print(f'Hello! You currently playing as {player1.name}.\n')
print(
    f'Your adventure begins {player1.player_room}... {player1.player_room.description}\n')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# Input parser
selection = 't'
while selection not in ['q']:
    selection = input(
        f'Location: {player1.player_room} | Type n, s, e, and w to move north, south, east, or west to move. Type q to quit.\n')
    try:
        selection = str(selection)
        if selection == 'n':
            print(f'You try to move north.')
            player1.move('n')
        elif selection == 's':
            print(f'You try to move south.')
            player1.move('s')
        elif selection == 'e':
            print(f'You try to move east.')
            player1.move('e')
        elif selection == 'w':
            print(f'You try to move west.')
            player1.move('w')
        elif selection == 'q':
            print("So long, partner!")
        else:
            print('Please type: n, s, e, w, or q!')
    except ValueError:
        print("Please enter one of the letters: n, s, e, w, or q")