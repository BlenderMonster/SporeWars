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
        self.emitterObject.name

    def createTileRepresentation(self, x, y, tile):
        self.emitterObject.localPosition.x = x
        self.emitterObject.localPosition.y = y
        if isinstance(tile, Food):
            tileRepresentation = context.scene.addObject(foodTypeRepresentations[tile.type], self.emitterObject)

