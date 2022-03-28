"""
Sun Jan 30 2022

Joe Kass
"""

#from Map import *
from enum import Enum

class Heading(Enum):
    North = "North"
    South = "South"
    East = "East"
    West = "West"

class Road:
    """Create Road to place objects in Traffic Sim"""
    
    road_count = 0
    
    def __init__(self, road_name, loc_x, loc_y, road_len, heading):
        """
        Parameters
        ----------
        road_name : STRING
            name of road
        loc_x : float
            location in x plane
        loc_y : float
            location in y plane
        road_len : float
            Length of Road
        heading : Heading Enum
            Direction of Road

        -------
        Init Road objec

        """
        pass
        if not isinstance(heading, Heading):
            raise TypeError('heading must be an instance of Heading Enum (North, South, East, West)')
            
        Road.road_count += 1
        
        self.name = road_name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.length = road_len
        self.heading = heading
        
        
    # def print_road(self): #not pythonic
    #     pass  