# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f'Room: {self.name}\nDescription: {self.description}'

    def item_grab(self, item_name):
        for item in self.inventory:
            if item_name == item_name:
                return item
            else:
                return None