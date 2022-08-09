#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import crayons

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # room descriptions
    if currentRoom == "Garden":
        print("Garden details")
    if currentRoom == "Kitchen":
        print("Kitchen details")
    if currentRoom == "Dining Room":
        print("Dining room details")
    if currentRoom == "Hall":
        print("Hall details")
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Garden',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'south' : 'Hall',
                  'east'  : 'Garden',
                  'west'  : 'Dining Room',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item' : 'shovel, rake',
                  'south' : 'Trap'
                }
        }


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            # added trap room the garden 
            if currentRoom == "Trap":
                print("You have fallen into a trap. There is no escape. Game over!")
                break
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print('You picked up ' + crayons.magenta(move[1]))
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        showStatus()
        print(crayons.red('A monster has got you... GAME OVER!'))
        break

        ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print(crayons.blue('You escaped the house with the ultra rare key and magic potion... YOU WIN!'))
        print(''' 
        ╔═══╗─────────────╔╗───╔╗───╔╗
        ║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗
        ║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
        ║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
        ║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
        ╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
        ──────────╔═╝║
        ──────────╚══╝
        ''')
        break



