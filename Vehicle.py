"""
Wed Jan 19 2022

Joe Kass
"""

class Traffic_Object:
    """Base class for simulation of traffic"""
    def __init__(self, speed, direction, location):
        self.speed = speed
        self.direction = direction
        self.location = location
    
    def accelerate(self, to_speed):
        pass
    
    def decelerate(self, to_speed):
        pass
    
    def turn(self, direction, degrees):
        pass

class Car(Traffic_Object):
    """Standard class for small motor vehicle"""
    def __init__(self, speed, direction, location):
        super().__init__(speed, direction, location)

class Truck(Traffic_Object):
    """Standard class for large motor vehicle"""
    def __init__(self, speed, direction, location, load_weight):
        super().__init__(speed, direction, location)
        self.load_weight = load_weight
        
    def set_load_weight(self, weight):
        self.load_weight = weight