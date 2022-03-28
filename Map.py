"""
Sun Jan 30 2022

Joe Kass
"""

from Road import Road
from SUI import Console_Print, Char_Matrix
#from GUI import *

class Map:
    """Create Map for objects in Traffic Sim"""
   
    
    def __init__(self):
        self._list_roads = []
        self.cm = Char_Matrix()
    
    def add_road(self, road):
        """include new road in map object"""
        if not isinstance(road, Road):
            raise TypeError("{} is not of type Road ".format(type(road)))
        
        self._list_roads.append(road)
    
    def print_map(self):
        """Print the map as provided"""
        for road in self._list_roads:
            Console_Print.print_road(self.cm, road)
            
    def display_map(self):
        """show the map in console"""
        for row in self.cm.char_map:
            for col in row:
                print(col, end="") 
            print()