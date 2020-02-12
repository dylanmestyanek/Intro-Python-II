class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'Item: {self.name}\nItem Description: {self.description}'
    
    def __repr__(self):
        return f'Item({repr(self.name)}, {repr(self.description)})'

    def on_take(self, item):
        return f'\n Woohoo! You have picked up {item} and added it to your inventory!\n'