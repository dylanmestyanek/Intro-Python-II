class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'\n>> {self.name}: {self.description}'

    def take_item(self):
        return f'\n---------------------------------------------------------------------------\n Woohoo! You have picked up {self.name} and added it to your inventory!\n---------------------------------------------------------------------------'