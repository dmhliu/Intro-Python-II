"""define the item class Item can be located in a room or
 carried by a player
"""
class Item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def print(self):
        print(self.name)
