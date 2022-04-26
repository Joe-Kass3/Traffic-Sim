"""
Sun Jan 30 2022

Joe Kass
"""

#from Map import *
from enum import Enum
from Road_Item import *

class Heading(Enum):
    North = 0
    South = 1
    East = 2
    West = 3

class Road:
    """Create Road to place objects in Traffic Sim"""
    
    road_count = 0
    
    def __init__(self, road_name, loc_x, loc_y, road_len, heading):
        """Standard Class for a Road Object"""
        if not isinstance(heading, Heading):
            raise TypeError('heading must be an instance of Heading Enum (North, South, East, West)')
            
        Road.road_count += 1
        
        self.name = road_name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.length = road_len
        self.heading = heading
        self._items = []
        
    def add_item(self, item):
        """Add item to """
        if not isinstance(item, Road_Item):
            raise TypeError("{} is not a Road Item object".format(type(item)))
        print(self.name)
        self._items.append(item)
        
        
          