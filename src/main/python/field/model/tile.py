__author__ = 'Monster'


class Tile():
    def __init__(self):
        pass

    @property
    def size(self):
        return (1,1)

class Food(Tile):
    def __init__(self, type):
        self.type = type

    @property
    def size(self):
        return (2,2)
