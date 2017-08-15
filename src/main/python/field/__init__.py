from field.views.bge import emitter

__author__ = 'Monster'

from mbge import context
from mutil import sensors
from field.model.field import Field
from field.model.tile import Food, Wall
from field.model.foodTypes import *
from field.model.model import Model
from field.views.bge.emitter import Emitter
from field.views.bge.fieldPresentation import FieldPresentation
import random

INTERNAL_PROPERTY_MODEL = "_internal.model"
INTERNAL_PROPERTY_REPRESENTATION = "_internal.representation"

PROPERTY_FIELD_WIDTH = "width"
PROPERTY_FIELD_HEIGHT = "height"
PROPERTY_TILE_EMITTER = "emitter"

OBJECT_TILE_EMITTER = "Tile.emitter"

def create():
    if not sensors.allPositive:
        return

    field = Field(
        context.owner[PROPERTY_FIELD_WIDTH],
        context.owner[PROPERTY_FIELD_HEIGHT])

    model = Model(field)

    emitterObject = findFieldEmitterObject()
    presentation = FieldPresentation(model, Emitter(emitterObject, field))
    context.owner[INTERNAL_PROPERTY_REPRESENTATION] = presentation

    model.addView(presentation)
    setupParticipatingObjects(model, presentation)

    model.addRandomFoodCores(5)


def landHere():
    if not sensors.allPositive:
        return

    hitObject = sensors.hitObjects[0]
    tile = getRepresentation().findTile(hitObject)
    getModel().createInitialWalls(tile)

def setupParticipatingObjects(model, presentation):
    context.owner[INTERNAL_PROPERTY_MODEL] = model
    for child in context.owner.children:
        child[INTERNAL_PROPERTY_MODEL] = model
        child[INTERNAL_PROPERTY_REPRESENTATION] = presentation


def addRandomFoodCores(amount):
    field = getModel().field
    for i in range(amount):
        x = random.randint(0, field.width)
        y = random.randint(0, field.height)
        type = random.randint(1,3)
        getModel().createTile(Food(x, y, type))


def getModel():
    return context.owner[INTERNAL_PROPERTY_MODEL]

def getRepresentation():
    return context.owner[INTERNAL_PROPERTY_REPRESENTATION]

def findFieldEmitterObject():
    for child in context.owner.children:
        if PROPERTY_TILE_EMITTER in child:
            return child
    error_message = "Object {} requires a child object with property {}".format(
        context.owner.name, PROPERTY_TILE_EMITTER)
    raise KeyError(error_message)
