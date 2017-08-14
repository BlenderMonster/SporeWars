__author__ = 'Monster'

from selectionModel import Selection, PropertyNotifier
from mbge import context
from mutil import sensors

INTERNAL_PROPERTY_SELECTION = "_selection"

def addHitObject():
    if not sensors.allPositive:
        return

    selection = getOrCreateSelection()
    hitObject = sensors.hitObjects[0]
    if hitObject in selection.selectedObjects:
        selection.deselect(hitObject)
    else:
        selection.select(hitObject)

def clear():
    if not sensors.allPositive:
        return

    try:
        selection = getSelection()
        selection.deselectAll()
    except KeyError:
        pass

def NandClear():
    if sensors.allPositive:
        return

    try:
        selection = getSelection()
        selection.deselectAll()
    except KeyError:
        pass

def getSelection():
    return context.owner[INTERNAL_PROPERTY_SELECTION]

def getOrCreateSelection():
    try:
        return getSelection()
    except KeyError:
        propertyName = getPropertyName()
        print(propertyName)
        selection = Selection(PropertyNotifier(propertyName))
        context.owner[INTERNAL_PROPERTY_SELECTION] = selection
        return selection

def getPropertyName():
    for sensor in context.controller.sensors:
        try:
            return sensor.propName
        except AttributeError:
            pass