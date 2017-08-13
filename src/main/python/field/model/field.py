__author__ = 'Monster'

from field.model.tile import Tile

class Field():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = {}

    def getTile(self, x, y):
        key = (x,y)
        try:
            return self.tiles[key]
        except KeyError:
            self.setTile(x, y, Tile())
        return self.tiles[key]

    def setTile(self, x, y, tile):
        for column in range(tile.size[0]):
            for row in range(tile.size[1]):
                self.tiles[x+column, y+row] = tile
