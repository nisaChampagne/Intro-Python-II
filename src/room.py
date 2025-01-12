from item import Item

# Implement a class to hold room information. This should have name and
# description attributes.

  ###Class Room has the following attributes
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
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        read = f'Room: {self.name}\nDescription: {self.description}'

        for i in self.items:
            read += f"\nAvailable Items: {i}. {i.description}"
        return read

    def add_item(self, item):
        return self.items.append(item)

    def delete_item(self, item):
        return self.items.remove(item)

    def get_items(self):
        return self.items