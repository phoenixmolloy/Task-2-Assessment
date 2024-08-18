from castle import Room
from item import Obj, Chest, Key
from character import Character, Boss


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

#Characters
dwarf = Character("Dwarf", "Small wise man with exceptional knowledge")
dwarf.set_conversation("")
dungeon.set_character(dwarf)
goblin = Character("Goblin", "A little greedy monster")
goblin.set_conversation("")
chapel.set_character(goblin)
wizard = Character("Wizard", "An old mysterious man who can perform magic spells and brew special potions")
wizard.set_conversation("")
labyrinth.set_character(wizard)
dragon = Boss("The Dragon", "-desc-")

#Objects
chest = Chest("Chest")
armor = Obj("Armor")
book = Obj("Enchanted Book")
key1 = Obj("Key 1")
key2 = Obj("Key 2")


#link objects to rooms
storage_room.set_obj(chest)
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


    obj = current_room.get_obj()
    if obj is not None:
        obj.describe()

    print("You are in: The " + current_room.get_name())
    current_room.describe()

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