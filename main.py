from castle import Room
from item import Obj
from character import Character, Enemy


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
great_hall.set_description("Spacious and heavenly room. More stairs in this room - requires different key ")

armory = Room("Armory")
armory.set_description("Filled with mostly empty armor stands ")

treasure_room = Room("Treasure Room")
treasure_room.set_description("Piles and piles of gold and treasure")

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
sword = Obj("sword")
armor = Obj("armor")
book = Obj("enchanted book")
key1 = Obj("Key 1")
key2 = Obj("Key 2")
fire_pot = Obj("fire Potion")


#Characters
dwarf = Character("Dwarf", "Small wise man with exceptional knowledge")
dwarf.set_conversation("Hello traveller. If you are here for the treasure, be aware of the dragon! Do not fight it without a sword and armor!")
dungeon.set_character(dwarf)
wizard = Character("Wizard", "An old mysterious man who can perform magic spells and brew special potions")
wizard.set_conversation("Dear traveller, I need a special book to help me finish making a potion. If you could help me, I will reward you.  {hint: find what he wants and 'give' to him")
labyrinth.set_character(wizard)
goblin = Enemy("Goblin", "A little greedy monster - Holding something shiny", "fire potion")
goblin.set_conversation("Grrrr!!")
chapel.set_character(goblin)



#link objects to rooms
storage_room.set_obj(sword)
armory.set_obj(armor)
library.set_obj(book)



#Game instructions
print("***************************************************************************")
print("You are at the bottom of a castle and must find your way to the ")
print("treasure at the top and defeat the dragon!")
print("Type the direction you want to go or the action you want to complete;")
print("(north, south, east, west, up, down, pick up, search, talk, fight, give)")
print("***************************************************************************")

bag = []
current_room = kitchen
dead = False
inhabitant_dead = False
enemy_dead = False
lock_1_open = False
lock_2_open = False
boss_defeated = False
dragon_health = 12

#Game loop
while dead == False:
    print("")
    print("You are in: The " + current_room.get_name())
    current_room.describe()
    obj = current_room.get_obj()
    inhabitant = current_room.get_character()

    #If enemy has died, they will not be in the room
    if enemy_dead == True:
        if inhabitant is goblin:
            inhabitant = None
    if inhabitant is not None:
        inhabitant.describe()

    current_room.get_details()

    #Boss fight
    if current_room is treasure_room:
        print("The Dragon has awoken!")
        print("Dragon Health:")
        print("♡" * dragon_health)
        choice = input("It is flying towards you. Do you choose to fight or run? ")
        if choice == "fight":
            for i in range(9):
                if dragon_health > 0:
                    choice2 = input("dodge, attack or block? ")
                    if choice2 == "dodge":
                        print("You successfully dodged the incoming attack and the dragon takes damage after flying into the ground.")
                        dragon_health = dragon_health - 1
                        print("Dragon Health:")
                        print("♡" * dragon_health)
                    elif choice2 == "attack":
                        choice3 = input("Go for the stomach, head or eye? ")
                        if sword in bag:
                            if choice3 == "head":
                                print("You went for the head and the dragon saw it coming. It bites your arm off and you bleed to death.")
                                exit()
                            elif choice3 == "stomach":
                                print("You found its weakpoint! A slash to the stomach is super effective")
                                dragon_health = dragon_health - 4
                                print("Dragon Health:")
                                print("♡" * dragon_health)
                            elif choice3 == "eye":
                                print("You have blinded the dragon and dealt damage to it. It can still attack you")
                                dragon_health = dragon_health - 2
                                print("Dragon Health:")
                                print("♡" * dragon_health)
                            else:
                                print("You can't hit there")
                        else:
                            print("You do not have a weapon. The dragon eats your head and you die.")
                            exit()
                    elif choice2 == "block":
                        if armor in bag:
                            print("Dragon shot fire at you. Your armor protects you.")
                        else:
                            print("You have no protection and you are fried by the dragons blast.")
                            exit()
                    else:
                        print("invalid move")
                else:
                    boss_defeated = True
            if dragon_health > 0:
                print("You are too exhausted from fighting. You collapse.")
                print("Game over")
                exit()
        else:
            print("Wrong choice. You have been burnt to a crisp.")
            exit()


    #Check every input if boss is dead or alive
    if boss_defeated == False:
        command = input("> ")
    if boss_defeated == True:
        print("Congratulations warrior! You have defeated the game and are rewarded with piles of treasure and gold!")
        exit()



    if command in ["north", "south", "east", "west", "up", "down"]:
        # current_room = current_room.move(command)
        #Can only go upstairs if user has key
        if command == "up":
            if current_room == kitchen:
                if lock_1_open == False:
                    if key1 in bag:
                        print("You used [key 1] to open the lock")
                        lock_1_open = True
                        bag.remove(key1)
                        current_room = current_room.move(command)
                else:
                    current_room = current_room.move(command)
            if current_room == great_hall:
                if lock_2_open == False:
                    if key2 in bag:
                        print("You used [key 2] to open the lock")
                        lock_2_open = True
                        bag.remove(key2)
                        current_room = current_room.move(command)
                else:
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
                elif weapon == "sword" and sword in bag:
                    print("The " + weapon + " is ineffective against the " + inhabitant.name)
                    print("You escape the goblin")
                else:
                    print("You don't have a " + weapon)
                    print(inhabitant.name + " has defeated you. Game Over")
                    dead = True
            else:
                print(inhabitant.name + " doesn't want to fight")
        else:
            print("There is nobody here to fight")