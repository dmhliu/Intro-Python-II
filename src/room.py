# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    valid_dirs = ('n','s','e','w')
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        
        #store neighbors by cardinal direction to.. per spec. not my idea
        
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        self.neighbor = {  # store 
                        'n' : self.n_to,
                        's' : self.s_to,
                        'e' : self.e_to,
                        'w' : self.w_to
                        }

    def __str__(self):
        return f"Room: {self.name} \n Description: {self.description}"
    def getname(self):
        return self.name
    def getdesc(self):
        return self.description
    def get_neighbor(self, dir=None):    
        """ check direction and return neighbor in dir ,
            incl None or False if bad dir, if dir = None, 
            return list of all Neighbors that are not None
        """
        if dir is None: 
            return [ f"{d} - {n.getname()}" for d,n in self.neighbor.items() if n is not None]
        elif dir in self.valid_dirs:
            return self.neighbor[dir] 
        else :
            return False
    def describe(self):
        return self.description

    def set_neighbor(self, dir, room):
        if dir in self.valid_dirs:
            self.neighbor[dir] = room   # todo validate room
            return True
        else:
            return False

