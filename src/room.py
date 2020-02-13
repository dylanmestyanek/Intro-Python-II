# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        s = f'Room Name: {self.name} \nDescription: {self.description} \n\n========================\n>>>  ITEMS IN ROOM  <<<\n========================'

        if len(self.items) > 0:
            for i in self.items:
                    s += f' {self.items[i]} '
        else:
            s += "\nNone"

        return s


    