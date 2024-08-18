
class Obj:
    def __init__(self, obj_name):
        self.name = obj_name
        self.description = None

    #Get the description of the item
    def get_description(self):
        return self.description

    #Set the description of the item
    def set_description(self, obj_description):
        self.description = obj_description

    #Get the name of the item
    def get_name(self):
        return self.name

    #Set the name of the item:
    def set_name(self, obj_name):
        self.name = obj_name

    def describe(self):
        print("The [" + self.name + "] is here - " + self.description)

class Key(Obj):
    def __init__(self, obj_name):
        super().__init__(obj_name)


class Chest(Obj):
    def __init__(self, obj_name):
        super().__init__(obj_name)
