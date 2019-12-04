# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"{self.name} is in {self.current_room}"

    def item_grab(self, item_name):
        for item in self.inventory:
            if item_name == item_name:
                return item
            else:
                return None

