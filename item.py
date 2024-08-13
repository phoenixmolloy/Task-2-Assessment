
class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    #Get the description of the item
    def get_description(self):
        return self.description

    #Set the description of the item
    def set_description(self, item_description):
        self.description = item_description

    #Get the name of the item
    def get_name(self):
        return self.name

    #Set the name of the item:
    def set_name(self, item_name):
        self.name = item_name

    def describe(self):
        print("The [" + self.name + "] is here - " + self.description)