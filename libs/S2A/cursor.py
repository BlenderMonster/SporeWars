
__version__ = "1.0"
__author__ = "Monster"

from mbge import context
from mutil import sensors

def toHitPosition():
    if not sensors.allPositive:
        return

    context.owner.worldPosition = sensors.hitPositions[0]


