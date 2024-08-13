from castle import Room
from item import Item
from character import Character


#Set the scene - room descriptions
storage_room = Room("Storage Room")
storage_room.set_description("Castle's junk and valuables ")

dungeon = Room("Dungeon")
dungeon.set_description("Dark and mysterious bunker ")

kitchen = Room("Kitchen")
kitchen.set_description("Stairs in this room - requires key ")

library = Room("Kitchen")
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
