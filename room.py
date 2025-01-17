class Room():
    def __init__(self,name_of_room):
        self.name = name_of_room
        self.description = None


    def get_description(self):
        return self.description

    def set_description(self,description):
        self.description = description