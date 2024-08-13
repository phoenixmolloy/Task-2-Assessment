
class Room:
    def __init__(self, room_name): #constructor
        self.name = room_name
        self.description = None
        self.linked_rooms = {}  # creates an empty dictionary
        self.character = None
        self.item = None

    #Method to get the name of the room:
    def get_name(self):
        return self.name

    #Method to set the name of the room:
    def set_name(self, room_name):
        self.name = room_name

    #Method to get the description of the room:
    def get_description(self):
        return self.description

    #Method to set the description of the room:
    def set_description(self, room_description):
        self.description = room_description

    #Will print out the object's description when it is called
    def describe(self):
        print(self.description)

    def describe(self):
        print(self.description)
    def link_rooms(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + Room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    #Method to get the character in a room:
    def get_character(self):
        return self.character

    #Method to set the character in a room:
    def set_character(self, room_character):
        self.character = room_character

    #Method to get the item in a room:
    def get_item(self):
        return self.item

    #Method to set the item in a room:
    def set_item(self, room_item):
        self.item = room_item