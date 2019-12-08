from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    ##Player receives the following attributes:  name, current_room, and items(as inventory)

    def __str__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        inventory = f"{self.name}'s Inventory: "

        for i in self.items:
            inventory += f"{i}, "
        return inventory

    ##will receive str  that returns the new_players inventory: containing the added items

    ###Player has the following methods: add and delete
        ##add will append the added item to the end of the list
        ##delete will remove the item 

    def add(self, item):
        return self.items.append(item)

    def delete(self, item):
        return self.items.remove(item)



