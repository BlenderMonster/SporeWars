__author__ = 'Monster'

from field.model.tile import Wall, Food
import random
import math

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

    def addRandomFoodCores(self, amount):
        field = self.field
        blockradius = 6
        split = 1

        kx = field.width
        ky = field.height
        while amount<kx*ky:
            kx = kx/2
            ky = ky/2

        numberOfColumns = math.ceil(kx)
        numberOfRows = math.ceil(ky)
        regions = random.sample(range(0, numberOfColumns * numberOfRows), amount)

        for region in regions:
            regionX = region % numberOfColumns
            regionY = region // numberOfRows
            regionWidth = field.width / numberOfColumns
            regionHeight = field.height / numberOfRows

            regionCenterX = int(regionX * regionWidth + regionWidth / 2)
            regionCenterY = int(regionY * regionHeight + regionHeight / 2)

            saveWidth = (regionWidth - blockradius) // 2
            saveHeight = (regionHeight - blockradius) // 2

            x = random.randint(regionCenterX - saveWidth, regionCenterX + saveWidth)
            y = random.randint(regionCenterY - saveHeight, regionCenterY + saveHeight)
            type = random.randint(1,3)
            self.createTile(Food(x, y, type))


