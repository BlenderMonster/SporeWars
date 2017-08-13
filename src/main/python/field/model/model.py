__author__ = 'Monster'

import random

class Model():
    def __init__(self, field, emitter):
        self.field = field
        self.emitter = emitter

    def addTileAtRandomLocation(self, food):
        field = self.field
        x = random.randint(0, field.width)
        y = random.randint(0, field.height)

        field.setTile(x, y, food)
        emitter.