
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
        print("[" + self.name + "] is here")

# class Enemy_loot(Obj):
#     def __init__(self, obj_name):
#         super().__init__(obj_name, current_room)
#         self.current_room = current_room

    # def drop(self, current_room):
    #     current_room.set_obj(object)


class Chest(Obj):
    def __init__(self, obj_name):
        super().__init__(obj_name)
