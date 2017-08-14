__author__ = 'Monster'

class Selection():
    def __init__(self, notifier = None):
        self.notifier = notifier
        self.selectedObjects = set()

    def select(self, object):
        self.selectedObjects.add(object)
        self.notifier.notify(object, True)

    def deselect(self, object):
        self.selectedObjects.remove(object)
        self.notifier.notify(object, False)

    def deselectAll(self):
        for object in  iter(self.selectedObjects.copy()):
            self.deselect(object)

class PropertyNotifier():
    def __init__(self, propertyName):
        self.propertyName = propertyName

    def notify(self, object, isSelected):
        object[self.propertyName] = isSelected
