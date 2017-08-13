__author__ = 'Monster'


class FieldPresentation():
    def __init__(self, model, emitter):
        self.tiles = {}
        self.emitter = emitter

    def findPresentation(self, tile):
        return self.tiles[tile]

    def createRepresentation(self, x, y, tile):
        self.emitter.createTileRepresentation(x, y, tile)