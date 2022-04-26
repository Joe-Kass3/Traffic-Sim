"""
Sun Jan 30 2022

Joe Kass
"""

from Road_Item import *

class Static_Road_Item(Road_Item):
    """Create static Traffic Sim items"""
    def __init__(self, mile_marker):
        super().__init__(mile_marker)
        
     
class Stop_Sign(Static_Road_Item):
    """Create a stop sign item"""
    def __init__(self, mile_marker):
        super().__init__(mile_marker)
    
class Intersection(Static_Road_Item):
      """Create an intersection item"""
      def __init__():
          pass  
      
class Speed_Limit_Sign(Static_Road_Item):
    """Create a speed limit sign item"""
    def __init__(self, posted_speed, mile_marker):
        super().__init__(mile_marker)
        self.posted_speed = posted_speed
    
class Yield_Sign(Static_Road_Item):
    """Create a yield sign item"""
    def __init__():
        pass