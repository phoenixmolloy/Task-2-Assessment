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
great_hall.link_rooms(chapel, "east")
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
wizard.set_conversation("help me get book")
labyrinth.set_character(wizard)
goblin = Enemy("Goblin", "A little greedy monster - Holding something shiny", "fire potion")
goblin.set_conversation("Grrrr!!")
chapel.set_character(goblin)
dragon = Boss("The Dragon", "-desc-")



#link objects to rooms
storage_room.set_obj(sword)
armory.set_obj(armor)
library.set_obj(book)



bag = []
current_room = kitchen
dead = False

#Game instructions
print("*****************************************************************")
print("You are at the bottom of a castle and must find your way to the ")
print("treasure at the top and defeat the dragon!")
print("Type the direction you want to go or the action you want to complete;")
print("(north, south, east, west, up, down, take, talk, )")
print("*****************************************************************")

#Game loop
while dead == False:
    print("")
    print("You are in: The " + current_room.get_name())
    current_room.describe()
    obj = current_room.get_obj()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    current_room.get_details()

    command = input("> ")


    if command in ["north", "south", "east", "west", "up", "down"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            if inhabitant is dwarf:
                print("[Dwarf says]: Take this key")
                bag.append(key1)
                print("You put [Key 1] in your bag")

        else:
            print("There's nobody here to talk to")

    elif command == "pick up":
        if obj is not None:
            print("You now have: " + obj.get_name())
            bag.append(obj)
            current_room.set_obj(None)
        else:
            print("Nothing here to pick up")

    elif command == "give":
        if inhabitant is wizard:
            if book in bag:
                print("[Wizard says]: Thank you, for your bravery I reward you with a special potion")
                bag.append("fire potion")
                print("You put the [fire potion] in your bag")
                bag.remove(book)
            else:
                print("You do not have what he wants")

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
                    if weapon ==:
                        print("You have successfully defeated the " + "-")
                        print("It dropped [Key 2]")
                        current_room.inhabitant = None
                        bag.append(key2)

                    else:
                        print(weapon + " is ineffective against the " + "-")
                else:
                    print("You don't have a " + weapon)
                    print("You die")
                    dead = True
            else:
                print(" -doesn't want to fight")
        else:
            print("There is nobody here to fight")

    # elif command == "take":
    #     if inhabitant




    elif command == "":
        print(bag)