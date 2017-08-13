from field.views.bge import emitter

__author__ = 'Monster'

__author__ = 'Monster'
from mbge import context
from mutil import sensors
from field.model.field import Field
from field.model.tile import Food
from field.model.foodTypes import *
from field.model.model import Model
from field.views.bge.emitter import Emitter
from field.views.bge.fieldPresentation import FieldPresentation
INTERNAL_PROPERTY_MODEL = "_internal.model"

PROPERTY_TILE_EMITTER  = "emitter"

def create():
    if not sensors.allPositive:
        return

    emitterObject = findFieldEmitterObject()
    emitter = Emitter(emitterObject)
    field = Field(50, 50)
    model = Model(field)
    presentation = FieldPresentation(model, emitter)

    model.addView(presentation)

    context.owner[INTERNAL_PROPERTY_MODEL] = model

    addRandomFoodCores(5)


def addRandomFoodCores(amount):
    field = getModel().field
    for i in range(amount):
        food = Food(FOOD_CRUMB)
        getModel().addTileAtRandomLocation(food)


def getModel():
    return context.owner[INTERNAL_PROPERTY_MODEL]

def findFieldEmitterObject():
    for child in context.owner.children:
        if PROPERTY_TILE_EMITTER in child:
            return child
    error_message = "Object {} requires a child object with property {}".format(
        context.owner.name, PROPERTY_TILE_EMITTER)
    raise KeyError(error_message)
