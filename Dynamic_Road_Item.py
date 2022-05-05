"""
Sun Jan 30 2022

Joe Kass
"""

from Road_Item import *
from enum import Enum

class Color(Enum):
    green = 0
    yellow = 1
    red = 2

class Dynamic_Road_Item(Road_Item):
    """Create dyanmic Traffic Sim items"""
    def __init__(self, mile_marker):
        super().__init__(mile_marker)

class Traffic_Light(Dynamic_Road_Item):
    """Create traffic light item"""
    def __init__(self, red_time, yellow_time, green_time, start_color, mile_marker):
        if not isinstance(start_color, Color):
            raise TypeError('Starting color must be an instance of Color Enum (green, yellow, red)')
        
        super().__init__(mile_marker)
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time
        self.current_color = start_color
        self.time_on = 0
        
    def update(self, time_on):
        self.time_on = (self.time_on + time_on) % (self.red_time + self.yellow_time + self.green_time) #shoud try to avoid incrementing forever
        
        while self.time_on > [self.green_time,self.yellow_time,self.red_time][self.current_color.value]:
            self.time_on -= [self.green_time,self.yellow_time,self.red_time][self.current_color.value]
            self.current_color = Color((self.current_color.value + 1) % 3)
