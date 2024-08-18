
class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.wants_to_fight = False
        self.bag = []

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

    def fight(self):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description, enemy_weakness):
        super().__init__(char_name, char_description)
        self.wants_to_fight = True
        self.weakness = enemy_weakness

    def get_weakness(self):
        return self.weakness

    #Set the name of the item:
    def set_weakness(self, enemy_weakness):
        self.weakness = enemy_weakness


    def fight(self, obj):
        if obj == self.weakness:
            print(self.name + " has been defeated with the " + obj)
            return True
        else:
            print(self.name + " killed you")
            return False

    # def loot(self):





class Boss(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.m = None