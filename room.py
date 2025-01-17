class Room():
    def __init__(self,name_of_room):
        self.name = name_of_room
        self.description = None
        self.linked_rooms = {}


    def get_description(self):
        return self.description

    def set_description(self,description):
        self.description = description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name