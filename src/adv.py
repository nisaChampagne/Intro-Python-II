from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, you see the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south.Dusty passages run north
and east."""),

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

# items
gameboy = Item("gameboy", "This is a gameboy, probably needs batteries")
batteries = Item("batteries", "Oh boy, some batteries!")
money = Item("money", "Oh boy $20!")
chair = Item("chair", "This is a chair...")
blanket = Item("blanket", "Oh look at that, its a blanket!")
pillow = Item("pillow", "This is a pillow.")


# appending items to rooms
room["foyer"].items = [gameboy]
room["overlook"].items = [batteries]
room["narrow"].items = [chair]
room["treasure"].items = [money]
room["outside"].items = [blanket]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Welcome pleb. What should I call you?: ")
new_player = Player(player_name, room["outside"])

# getitem()
def getitem():
    item_choice = input("What do you want to do? Ex: get sword: ").split()
    for i in new_player.current_room.items:
        if item_choice[1] == i.name and item_choice[0] == "get":
            new_player.items.append(i)
            new_player.current_room.items.remove(i)
        else:
            print("Option not available.")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#


game_status = True
while game_status:
    cmd = input('\nLets explore... ==>')
    try:
        # lets you test code for errors
        if cmd == "q":
            print(f'Thats fine, Go home {new_player.name}!')
            game_status = False
        if cmd == 'n' or cmd == 'e' or cmd == 's' or cmd == 'w':
            direction = f'{cmd}_to'
            if new_player.current_room.__dict__[direction] == None:
                print("Cannot move in that direction.")
            else:
                new_player.current_room = new_player.current_room.__dict__[
                    direction]
                print(new_player.current_room)
                if len(new_player.current_room.items) > 0:
                    getitem()
                    print(new_player)
                    if len(new_player.items) == 5:
                        print(f"{new_player.name}, you found all the things!")
                        break
    except ValueError:
        # handles the error
        print('Invalid command.\n')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
