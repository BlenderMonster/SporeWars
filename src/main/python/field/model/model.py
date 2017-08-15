__author__ = 'Monster'

from field.model.tile import Wall

class Model():
    def __init__(self, field):
        self.field = field
        self.views = []

    def createTile(self, tile):
        self.field.setTile(tile.x, tile.y, tile)
        for view in self.views:
            view.createRepresentation(tile.x, tile.y, tile)

    def addView(self, view):
        self.views.append(view)

    def createInitialWalls(self, food):
        for a in range(8):
            self.createTile(Wall(food.x-4+a, food.y-4))
            self.createTile(Wall(food.x-4+a, food.y+3))

        for a in range(6):
            self.createTile(Wall(food.x-4, food.y-3+a))
            self.createTile(Wall(food.x+3, food.y-3+a))