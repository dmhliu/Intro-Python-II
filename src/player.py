# Write a class to hold player information, e.g. what room they are in
# currently.
import sys
class Player:
    def __init__(self, name='john doe', room=None): 
        
        self.name = name
        self.room = room 
        self.inventory = [] 
    def __str__(self):
        return self.name
    def report(self):
        print(f"\n\n.....{self.name} is in {self.room.getname()}")
        print(f"\n'{self.room.describe()}'")
        print(f"you can see some things on the floor.. \n looks like there is"
              f"{self.room.getinventorynames()}")
        print(f"\n...what has it got in its pocketsses? \n{self.getinventorynames()}")

    def getname(self):
        return self.name
    def setname(self, newname):
        self.name = newname
    def getlocationname(self):
        return self.room.getname()
    def getlocation(self):
        return self.room
    def getinventory(self):
        if self.inventory:
            return self.inventory
        else: 
            return False
    def getinventorynames(self):
        if self.inventory:
            return [item.name for item in self.inventory]
    
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
            print(f"..you move {direction}, and enter {self.room})")
            print(f"\n\n... you see the following objects:",
                f" {[item.name for item in self.room.getinventory()]}")

            return True
        else:
            return False
    def pickup(self,itemname):
        # validate item is present in room
        thething = self.room.remove_item(itemname) # if itemname is found, will ret the obj
        if thething:
            print(f"item {itemname} was picked up")
            self.inventory.append(thething)    
            return True
        else:
            print(" ... * poof * ... that {item} disappears before you can grab it!")
            return False
    def drop(self,itemname):                 
         # validate item is present in self.inventory
        inv_names = [i.name for i in self.inventory]
        d = dict(zip(inv_names,self.inventory))
        the_item = d[itemname]
        if the_item:  
            try:
                self.inventory.remove(the_item)
                return True
            except ValueError:
                print(f"\n.\n.\n...sorry, can't drop it if you dont got it!!!")
        else:
            print(f"\n.\n.\n...sorry, can't drop it if you dont got it!!!")
            return False
   





        