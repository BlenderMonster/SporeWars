__author__ = 'Monster'


class FieldPresentation():
    def __init__(self, model, emitter):
        self.tiles = {}
        self.emitter = emitter

    def findPresentation(self, tile):
        return self.tiles[tile]

    def createPresentation(self, tile):
        self.emitter.createTileRepresentation(tile)