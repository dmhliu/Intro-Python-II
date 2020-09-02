# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name='john doe', room=room['outside']): 
        """create player in a room, default to outside"""
        self.name = name
        self.room = room
    def getname(self):
        return self.name
    def getlocation(self):
        return self.room.getname()
        

        