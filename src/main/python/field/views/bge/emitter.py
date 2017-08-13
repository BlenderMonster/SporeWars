__author__ = 'Monster'

from mbge import context
from field.model.foodTypes import *
from field.model.tile import Food

foodTypeRepresentations = {
    FOOD_CRUMB: "Food.Crumb.bread",
    FOOD_BAR: "Food.Bar",
    FOOD_BLOB: "Food.Blob",
}

class Emitter():
    def __init__(self, emitterObject):
        self.emitterObject = emitterObject

    def createTileRepresentation(self, tile):
        if isinstance(tile, Food):
            tileRepresentation = context.scene.addObject(foodTypeRepresentations[tile.type], self.emitterObject)

