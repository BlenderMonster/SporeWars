__author__ = 'Monster'


class FieldPresentation():
    def __init__(self, model, emitter):
        self.tiles = {}
        self.representations = {}
        self.emitter = emitter

    def findPresentation(self, tile):
        return self.tiles[tile]

    def createRepresentation(self, x, y, tile):
        representation = self.emitter.createTileRepresentation(x, y, tile)
        self.tiles[tile] = representation
        self.representations[representation] = tile

    def findTile(self, representation):
        return self.representations[representation]