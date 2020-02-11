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
        s = f'Room Name: {self.name} \nDescription: {self.description} \nItems in room: '

        if len(self.items) > 0:
            for i in self.items:
                if  self.items.index(i) == (len(self.items) - 1):
                    s += f'and {i}.'
                else:
                    s += f'{i}, '
        else:
            s += "None"

        return s

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'
    