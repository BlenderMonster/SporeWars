'''
The Sensor-To-Actuator library
==============================

This module provides functions to transfer results from sensors
to actuators, sets position or aligns to a vector
'''
__version__ = "2.0"
__author__ = "Monster"

from mbge import context
from mutil import sensors

PROPERTY_AXIS = "axis"; DEFAULT_AXIS = "X"
PROPERTY_FACTOR = "factor"; DEFAULT_FACTOR = 1.0

X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

AXIS_VALUE_TO_AXIS_MAPPING = {
    "X": X_AXIS,
    "Y": Y_AXIS,
    "Z": Z_AXIS
}

def hitObjectToObject():
    hitObject = _findClosestObject()

    for actuator in context.controller.actuators:
        try:
            actuator.object = hitObject
        except AttributeError:
            pass

def hitObjectToTarget():
    hitObject = _findClosestObject()

    for actuator in context.controller.actuators:
        try:
            actuator.target = hitObject
        except AttributeError:
            pass

def hitPositionToPosition():
    hitObject = _findClosestObject()

    if not hitObject:
        return

    for actuator in context.controller.actuators:
        actuator.owner.worldPosition = hitObject.position

def hitNormalToAlign():
    sensor =_findSensorToClosestObject()

    if not sensor:
        return

    hitNormal = sensor.hitObject
    axisValue = context.owner.get(PROPERTY_AXIS, DEFAULT_AXIS)
    axis = AXIS_VALUE_TO_AXIS_MAPPING[axisValue]
    factor = context.owner.get(PROPERTY_FACTOR, DEFAULT_FACTOR)

    for actuator in context.controller.actuators:
        actuator.owner.alignAxisToVect(hitNormal.worldOrientation.col[0], axis, factor)

def _findClosestObject():
    hitObjects = sensors.hitObjects
    return min(hitObjects, key=lambda object: object.getDistanceTo(context.owner))

def _findSensorToClosestObject():
    sensorToClosestObject = None
    for sensor in context.controller.sensors:
        try:
            hitObject = sensor.hitObject
            if (sensorToClosestObject or
                hitObject.getDistanceTo(context.owner)<sensorToClosestObject.getDistanceTo(context.owner)):
                sensorToClosestObject = sensor
        except AttributeError:
            continue
    return sensor
