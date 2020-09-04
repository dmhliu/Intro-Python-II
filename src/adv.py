import re
import os
from room import Room
from player import Player
from item import Item
import random

with open('nounlist.txt',mode='r') as f:
    NOUNS = f.read().splitlines()
def setup():
    """ Setup a new game by populating list of rooms
    linking rooms 
    create new player
    returns : new player instance 
    """
    room = {
        'outside':  Room("Outside Cave Entrance",
                        "North of you, the cave mount beckons"),
        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),
        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),
        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),
        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
    }
    # Link rooms together  
    # why are we setting instance vars directly, isnt this not strict OOP

    room['outside'].set_neighbor('n', room['foyer'])

    room['foyer'].set_neighbor('s', room['outside'])
    room['foyer'].set_neighbor('n', room['overlook'])
    room['foyer'].set_neighbor('e', room['narrow'])
    room['overlook'].set_neighbor('s', room['foyer'])
    room['narrow'].set_neighbor('w', room['foyer'])
    room['narrow'].set_neighbor('n', room['treasure'])
    room['treasure'].set_neighbor('s', room['narrow'])
    # Make a new player object that is currently in the 'outside' room.

    rand_names = random.sample(NOUNS, 10) # get 10 random item names
    for name in rand_names:
        random.choice(list(room.values())).add_item(Item(name)) 
    return Player(name=None, room=room['outside']) # starts outside by default

def main():
    """main function for game
    """
    validinputs =  ['n','s','e','w','i','q']  
    directions = ['n','s','e','w']
    
    def parse(raw):
        raw = raw.lower() # normalize to lcase

        REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
        BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
        stopwords = ['a', 'an', 'that', 'the', 'teh', 'yonder', 'to', 'want']

        if len(raw.split(' ')) == 1 :   
            return [raw]
        else: 
            text = REPLACE_BY_SPACE_RE.sub(' ', raw)  # symbols by space in text
            text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE
            tokens = [t for t in text.split(' ') if t not in stopwords]  # split command into words and remove garbage
            return tokens 
    
    # interactive loop
    newplayer = setup() 
    pname = input("Please give your player a name: ")
    newplayer.setname(pname)
    newplayer.report()

    CMDS = {newplayer.pickup: ['pickup', 'grab','snatch', 'get','take'],
            newplayer.drop:  ['drop', 'yeet', '86', 'ditch'],
            newplayer.move_to: ['go','move','run'],
            exit: ['q', 'quit', 'adios', 'bye'],
            newplayer.report: ['report', 'sitrep'],
            newplayer.getinventorynames: ['i','shakedown', 'inventory', 'inv']    # player inv
            }
    while True: 
    # * Waits for user input and decides what to do.
        rawinput = input("what is your bidding? [n|s|e|w|q] : \n")
        parsed_arg_it = iter(parse(rawinput))
        arg = next(parsed_arg_it) # get first arg
        if  arg in directions:  # handle legacy shortcuts
            if newplayer.move_to(arg):
                print(f"{newplayer} moved to the {newplayer.getlocationname()}")
            else:
                print(f".\n..\n...\n....yeah, nope. there no room in that direction!")
                print(f"HINT: try {newplayer.getlocation().get_neighbor()}")
        elif True:
            for cmd, alias in CMDS.items():
                if arg in alias:
                    try: 
                        a = next(parsed_arg_it)   # is there a following arg?
                        if cmd(a):
                            break
                        else:
                            print(f"You can {arg} , but you cant {arg} {a}")
                    except StopIteration:  # only 1 arg try to execute
                        try:
                            cmd()
                            break
                        except:
                            print("\n....... hmm. I was expecting more from you.\n")            
                else:  #couldnt interperet the token, complain
                    print(f"\n Eh??? \n\t Whaddya say? {arg} ??"
                        f" Sorry I don't know what to do about that.")
if __name__ == "__main__":
    main()