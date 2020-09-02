from room import Room
from player import Player


#
def main():
    # Declare all the rooms

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

    room['outside'].n_to = room['foyer']

    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']

    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']
#### my way 
    room['outside'].set_neighbor('n', room['foyer'])

    room['foyer'].set_neighbor('s', room['outside'])
    room['foyer'].set_neighbor('n', room['overlook'])
    room['foyer'].set_neighbor('e', room['narrow'])
    room['overlook'].set_neighbor('s', room['foyer'])
    room['narrow'].set_neighbor('w', room['foyer'])
    room['narrow'].set_neighbor('n', room['treasure'])
    room['treasure'].set_neighbor('s', room['narrow'])
    # Make a new player object that is currently in the 'outside' room.

    pname = input("Please give your player a name: ")
    newplayer = Player(name=pname, room=room['outside']) # starts outside by default
    validinputs =  ['n','s','e','w','q']  

    def debug(player=None):
        print(f"[DEBUG]rooms dict: {room.keys()}")
        if player:
            print(f"[DEBUG]current player is {player}")
            print(f"[DEBUG]current room and neighbors: \n {player.room} \n {player.room.neighbor}")
    # Write a loop that:
    while True: 
    # * Prints the current room name   #assume this means the room that the current player is in.

        print(f"\n.....{newplayer.getname()} is in {newplayer.getlocationname()}")

    # * Prints the current description (the textwrap module might be useful here).
        print(f"'{newplayer.getlocation().describe()}'")
    # * Waits for user input and decides what to do.
    #   
        rawinput = input("Where to? [n|s|e|w|q] : ")
        # test input
        try:  # make it throw and error for fun
            _ = validinputs.index(rawinput)
        except ValueError: 
            print (f"\n Sorry, I didn't understand that! \nPlease Enter one of the following {validinputs}")
            continue
        if rawinput == 'q' :
            print(f"{newplayer} says 'live long and prosper! \/' ")
            break
        else:
            if newplayer.move_to(rawinput):
                print(f"{newplayer} moved to the {newplayer.getlocationname()}")
            else:
                print(f".\n..\n...\n\....yeah, nope. there no room in that direction!")
                print(f"HINT: try {newplayer.getlocation().get_neighbor()}")
        # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.print
if __name__ == "__main__":
    main()