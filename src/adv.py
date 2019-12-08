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
earlier adventurers. The exit is to the south but you can head north down a little
hallway for a surprise...."""),

    'hogwarts': Room("Hogwarts", """It is real!
You're a wizard after all! You can choose to go back south if you'd like....muggle"""),
}

# items
items = {
"gameboy": Item("gameboy", "This is a gameboy, probably needs batteries"),
"batteries": Item("batteries", "Oh boy, some batteries!"),
"money": Item("money", "Oh boy $20!"),
"chair": Item("chair", "This is a chair..."),
"blanket": Item("blanket", "Oh look at that, its a blanket!"),
"pillow": Item("pillow", "This is a pillow."),
"wand": Item("wand", "I guess you're officially a wizard....")
}

# using add_item method to add item(s) to rooms
room["foyer"].add_item(items["gameboy"])
room["overlook"].add_item(items["batteries"])
room["narrow"].add_item(items["chair"])
room["treasure"].add_item(items["money"])
room["outside"].add_item(items["blanket"])
room["outside"].add_item(items["pillow"])
room["hogwarts"].add_item(items["wand"])


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['hogwarts']
room['hogwarts'].s_to = room['treasure']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Welcome pleb. What should I call you?: ")
new_player = Player(player_name, room["outside"])


# getitem()
def getitem():
    item_choice = input(f"You found a thing, would you like to pick it up? Ex: get sword: ").split()
    for item in new_player.current_room.items:
        if item_choice[1] == item.name and item_choice[0] == "get":
            new_player.current_room.delete_item(item)
            new_player.add(item)
            Item.take(item)
        else:
            print("Not an existing choice.")

# dropitem()
def dropItem():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    prompt = input("Would you like to drop some things off?: ex yes or no   ")
    if prompt == "yes":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        drop_item = input("What would you like to drop? Ex: drop sword: ").split()
        for item in new_player.items:
            if drop_item[1] == item.name and drop_item[0] == "drop":
                new_player.current_room.add_item(item)
                new_player.delete(item)
                Item.drop(item)
            else:
                print("Try again?")
    elif prompt == "no":
        print("Thats fine")
    else:
        print("Not a valid choice")



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#


game_status = True
while game_status:

    ##winners conditions
    if len(new_player.items) == 7:
        print(f"{new_player.name}, you found all the things!")
        break

    #intro prompt
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    cmd = input('\nLets explore... ==>')
    # try lets you test code for errors
    try:
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
                if len(new_player.current_room.items) >= 1:
                    getitem()
                    print(new_player)
                    if len(new_player.current_room.items) == 0:
                        dropItem()
                        print(new_player)
                else:
                    print("error dropping")
    # except handles the error
    except ValueError:
        print('Invalid command.\n')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
