__author__ = 'Monster'

import unittest

from field.field import Field
from field.model.tile import Tile


class FactoryTestCase(unittest.TestCase):
    def test_Field_getUnknownTile(self):

        field = Field(100,100)
        tile = field.getTile(1,2)
        self.assertIsNotNone(tile)

    def test_Field_setTile(self):

        field = Field(100, 100)
        tile = Tile()
        field.setTile(3,4, tile)
        self.assertEqual(tile, field.getTile(3, 4))