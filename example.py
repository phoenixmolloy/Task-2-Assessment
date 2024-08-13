
##main
from main import Room
from character import Enemy, Friend
from character import Character
from item import Item


#room descriptions
storage_room = Room("Storage Room")
storage_room.set_description("Castle's junk and valuables ")

dungeon = Room("Dungeon")
dungeon.set_description("Dark and mysterious bunker ")

kitchen = Room("Kitchen")
kitchen.set_description("Stairs in this room - requires key ")

library = Room("Kitchen")
library.set_description("endless knowledge and books ")

labyrinth = Room("Labyrinth")
labyrinth.set_description("")





cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")




harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")
grotto.set_item(vegemite)
torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
dungeon.set_item(torch)


bag = []
current_cave = cavern
dead = False

while dead == False:
    print("\n")

    item = current_cave.get_item()
    if item is not None:
        item.describe()

    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)

    elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Bravo, hero you won the fight!")
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True
                else:
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")

    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)


##castle
#Create Room class
class Room:
    def __init__(self, room_name): #constructor
        self.name = room_name
        self.description = None
        self.linked_rooms = {}  # creates an empty dictionary
        self.character = None
        self.item = None

    #Here is a method to get the description of the cave:
    def get_description(self):
        return self.description

    #Here is a method to set the description of the cave:
    def set_description(self, room_description):
        self.description = room_description

    #Will print out the object's description when it is called
    def describe(self):
        print(self.description)

    #Here is a method to get the name of the cave:
    def get_name(self):
        return self.name

    #Here is a method to set the name of the cave:
    def set_name(self, room_name):
        self.name = room_name

    def describe(self):
        print(self.description)

    # Add link_cave method here
    def link_cave(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    #Here is a method to get the character in a cave:
    def get_character(self):
        return self.character

    #Here is a method to set the character in a cave:
    def set_character(self, room_character):
        self.character = room_character

    #Here is a method to get the item in a cave:
    def get_item(self):
        return self.item

    #Here is a method to set the item in a cave:
    def set_item(self, cave_item):
        self.item = cave_item