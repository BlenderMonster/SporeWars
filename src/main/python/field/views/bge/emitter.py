__author__ = 'Monster'

from mbge import context
from field.model.foodTypes import *
from field.model.tile import Food, Wall

foodTypeMeshes = {
    FOOD_CRUMB: "Food.Crumb.bread",
    FOOD_BAR: "Food.Bar",
    FOOD_BLOB: "Food.Blob",
}
OBJECT_TILE_WALL = "Wall.block"
OBJECT_TILE_FOOD_CLICKABLE = "Food.clickable"
OBJECT_TILE_FOOD = "Food"

class Emitter():
    def __init__(self, emitterObject, field):
        self.emitterObject = emitterObject
        emitterObject.name
        self.field = field

    def createTileRepresentation(self, x, y, tile):
        emitterObject = self.emitterObject
        emitterObject.localPosition.x = x
        emitterObject.localPosition.y = y

        if isinstance(tile, Food):
            tileRepresentation = context.scene.addObject(OBJECT_TILE_FOOD_CLICKABLE, self.emitterObject)
            tileRepresentation.worldScale = [1, 1, 1]
            tileRepresentation.children[OBJECT_TILE_FOOD].replaceMesh(foodTypeMeshes[tile.type])
            return tileRepresentation

        if isinstance(tile, Wall):
            tileRepresentation = context.scene.addObject(OBJECT_TILE_WALL, self.emitterObject)
            tileRepresentation.worldScale = [1, 1, 1]
            return tileRepresentation

