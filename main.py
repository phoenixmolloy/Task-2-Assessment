from castle import Room
from item import Obj, Chest
from character import Character, Enemy, Boss


#Set the scene - room descriptions
storage_room = Room("Storage Room")
storage_room.set_description("Castle's junk and valuables ")

dungeon = Room("Dungeon")
dungeon.set_description("Dark and mysterious bunker ")

kitchen = Room("Kitchen")
kitchen.set_description("Stairs in this room - requires key ")

library = Room("Library")
library.set_description("Endless knowledge and books ")

labyrinth = Room("Labyrinth")
labyrinth.set_description("Smells of magic and mystery")

chapel = Room("Chapel")
chapel.set_description("Holy room for prayers and worshiping ")

great_hall = Room("Great Hall")
great_hall.set_description("Spacious and heavenly room ")

armory = Room("Armory")
armory.set_description("Filled with mostly empty armor stands ")

treasure_room = Room("Treasure Room")
treasure_room.set_description("Piles and piles of gold and treasure ")

#Link rooms together
#Floor level 1
storage_room.link_rooms(kitchen, "south")
storage_room.link_rooms(dungeon, "east")
dungeon.link_rooms(storage_room, "west")
dungeon.link_rooms(library, "south")
library.link_rooms(dungeon, "north")
library.link_rooms(kitchen, "west")
kitchen.link_rooms(storage_room, "north")
kitchen.link_rooms(library, "east")
kitchen.link_rooms(great_hall, "up")

#Floor level 2
labyrinth.link_rooms(great_hall, "south")
labyrinth.link_rooms(chapel, "east")
chapel.link_rooms(labyrinth, "west")
chapel.link_rooms(armory, "south")
armory.link_rooms(chapel, "north")
armory.link_rooms(great_hall, "west")
great_hall.link_rooms(labyrinth, "north")
great_hall.link_rooms(armory, "east")
great_hall.link_rooms(treasure_room, "up")
great_hall.link_rooms(kitchen, "down")


#Objects
sword = Obj("Sword")
armor = Obj("Armor")
book = Obj("Enchanted Book")
key1 = Obj("Key 1")
key2 = Obj("Key 2")
fire_pot = Obj("Fire Potion")


#Characters
dwarf = Character("Dwarf", "Small wise man with exceptional knowledge")
dwarf.set_conversation("Hello traveller. If you are here for the treasure, be aware of the dragon! Do not fight it without protection and a weapon!")
dungeon.set_character(dwarf)
wizard = Character("Wizard", "An old mysterious man who can perform magic spells and brew special potions")
wizard.set_conversation("Dear traveller, I need a special book to help me finish making a potion. If you could help me, I will reward you")
labyrinth.set_character(wizard)
goblin = Enemy("Goblin", "A little greedy monster - Holding something shiny", "fire potion")
goblin.set_conversation("Grrrr!!")
chapel.set_character(goblin)
dragon = Boss("The Dragon", "-desc-")



#link objects to rooms
storage_room.set_obj(sword)
armory.set_obj(armor)
library.set_obj(book)

#Game instructions
print("***************************************************************************")
print("You are at the bottom of a castle and must find your way to the ")
print("treasure at the top and defeat the dragon!")
print("Type the direction you want to go or the action you want to complete;")
print("(north, south, east, west, up, down, search, pick up, talk, fight, give)")
print("***************************************************************************")

bag = []
current_room = kitchen
dead = False
inhabitant_dead = False
enemy_dead = False
lock_1_open = False
lock_2_open = False

#Game loop
while dead == False:
    print("")
    print("You are in: The " + current_room.get_name())
    current_room.describe()
    obj = current_room.get_obj()
    inhabitant = current_room.get_character()

    if enemy_dead == True:
        if inhabitant is goblin:
            inhabitant = None

    if inhabitant is not None:
        inhabitant.describe()

    current_room.get_details()

    command = input("> ")


    if command in ["north", "south", "east", "west", "up", "down"]:
        #Can only go upstairs if user has key
        if command == "up":
            if current_room == kitchen:
                if lock_1_open == False:
                    if key1 in bag:
                        print("You used [key 1] to open the lock")
                        lock_1_open = True
                        bag.remove(key1)
                        current_room = current_room.move(command)
            if current_room == great_hall:
                if lock_2_open == False:
                    if key2 in bag:
                        print("You used [key 2] to open the lock")
                        lock_2_open = True
                        bag.remove(key2)
                        current_room = current_room.move(command)
            else:
                print("You need a key to open the lock on the stairs. ")
        if command != "up":
            current_room = current_room.move(command)

    #Conversation with any character
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            if inhabitant is dwarf:
                print("[Dwarf says]: Take this key")
                bag.append(key1)
                print("You put [key 1] in your bag")

        else:
            print("There's nobody here to talk to")

    #Collects an item and adds to bag
    elif command == "pick up":
        if obj is not None:
            print("You now have: " + obj.get_name())
            bag.append(obj)
            current_room.set_obj(None)
        else:
            print("Nothing here to pick up")

    #To give a character an item from bag
    elif command == "give":
        if inhabitant is not None:
            if inhabitant is wizard:
                if book in bag:
                    print("[Wizard says]: Thank you, for your bravery I reward you with a special potion")
                    bag.append("fire potion")
                    print("You put the [fire potion] in your bag")
                    bag.remove(book)
                else:
                    print("You do not have what he wants")
            else:
                print("The " + inhabitant.name + " doesn't want anything")

    #Tells user if there is anything to pick up in the room
    elif command == "search":
        if obj is not None:
            obj.describe()
        else:
            print("No objects here")

    #Fight - Happens only if there is an enemy to fight
    elif command == "fight":
        if inhabitant is not None:
            if inhabitant.wants_to_fight == True:
                print("What will you fight with?")
                weapon = input("> ")
                if weapon in bag:
                    if weapon == inhabitant.weakness:
                        print("You have successfully defeated the " + inhabitant.name)
                        print("It dropped [key 2]")
                        print("[key 2] is now in bag")
                        bag.append(key2)
                        bag.remove(inhabitant.weakness)
                        # current_room.inhabitant = None
                        enemy_dead = True
                    else:
                        print(weapon + " is ineffective against the " + inhabitant.name)
                        print(inhabitant.name + " has defeated you. Game Over")
                        dead = True
                else:
                    print("You don't have a " + weapon)
                    print(inhabitant.name + " has defeated you. Game Over")
                    dead = True
            else:
                print(inhabitant.name + " doesn't want to fight")
        else:
            print("There is nobody here to fight")




    elif command == "":
        print(bag)