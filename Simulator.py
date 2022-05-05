"""
Sun Jan 30 2022

Joe Kass
"""
from Dynamic_Road_Item import Traffic_Light

class Simulation:
    """Create simulator for Traffic Sim"""
    def __init__(self):
        self._dynamic_objects = []

    def add_dynamic_object(self, dynamic_object):
        self._dynamic_objects.append(dynamic_object)
        
    def update(self, time):
        for obj in self._dynamic_objects:
            obj.update(time) #only updating traffic light for now