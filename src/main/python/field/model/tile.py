__author__ = 'Monster'


class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def size(self):
        return (1, 1)

class Food(Tile):
    def __init__(self, x, y, foodType):
        super().__init__(x, y)
        self.type = foodType

    @property
    def size(self):
        return (2, 2)

class Wall(Tile):
    pass