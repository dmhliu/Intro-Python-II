# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name='john doe', room=None): 
        """create player in a room, default to outside"""
        self.name = name
        self.room = room
    def __str__(self):
        return self.name
    def getname(self):
        return self.name
    def getlocationname(self):
        return self.room.getname()
    def getlocation(self):
        return self.room

    def __set_room__(self, newroom): # use a private method to set
        self.room = newroom
    def move_to(self, direction):
        """try to move to the room neighboring in {direction} of 
        the players current room
        direction : string {n,s,e,w}
        return : bool True if current room neighbor exists else False
        """
        
        if self.room.neighbor[direction]:  #check if room in dir exists
            self.__set_room__(self.room.neighbor[direction])
            return True
        else:
            return False




        