# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        
        #store neighbors by cardinal direction to.. per spec. not my idea
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"Room: {self.name} \n Description: {self.description}"
    def getname(self):
        return self.name
    
