"""
Sun Jan 30 2022

Joe Kass
"""
from abc import ABC, abstractmethod
#from Road import *

class Road_Item(ABC):
    """Create list of possible Traffic Sim items"""
    def __init__(self, mile_marker):
        self.mile_marker = mile_marker