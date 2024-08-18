
class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( "A " + self.name + " is here!")
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " can't talk to you")

    def take(self):
        print("You took from " + self.name)



    # Fight with this character
    # def fight(self):
    #
    # def fight(self):

class Boss(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.m = None