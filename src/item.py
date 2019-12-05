class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def take(self):
        print("You have picked up " + self.name)

    def drop(self):
        print("You have dropped " + self.name)