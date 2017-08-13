__author__ = 'Monster'

import random

class Model():
    def __init__(self, field):
        self.field = field
        self.views = []

    def addTileAtRandomLocation(self, tile):
        field = self.field
        x = random.randint(0, field.width)
        y = random.randint(0, field.height)

        field.setTile(x, y, tile)
        for view in self.views:
            view.createRepresentation(x, y, tile)


    def addView(self, view):
        self.views.append(view)
