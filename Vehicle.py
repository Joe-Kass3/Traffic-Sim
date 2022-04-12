"""
Wed Jan 19 2022

Joe Kass
"""

from abc import ABC, abstractmethod
from Common import Constants

class Vehicle(ABC):
    """Base class for simulation of traffic"""
    def __init__(self, speed, desired_speed, direction, location):
        self.speed = speed
        self.desired_speed = desired_speed
        self.direction = direction
        self.location = location
    
    @abstractmethod
    def accelerate(self, seconds):
        ...
    
    @abstractmethod
    def decelerate(self, seconds):
        ...
    
    @abstractmethod
    def turn(self, direction, degrees):
        ...

    def update_speed(self, seconds):
        if (self.speed > self.desired_speed):
            self.decelerate(seconds)
        elif (self.speed < self.desired_speed):
            self.accelerate(seconds)


class Car(Vehicle):
    """Standard class for small motor vehicle"""
    def __init__(self, speed, desired_speed, direction, location):
        super().__init__(speed, desired_speed, direction, location)
    
    def accelerate(self, seconds):
        temp_speed = self.speed + (Constants.ACC_RATE * seconds * Constants.MPS_TO_MPH)
        if (temp_speed > self.desired_speed):
            self.speed = self.desired_speed
        else:
            self.speed = temp_speed

    def decelerate(self, seconds):
        temp_speed = self.speed - (Constants.DEC_RATE * seconds * Constants.MPS_TO_MPH)
        if (temp_speed < self.desired_speed):
            self.speed = self.desired_speed
        else:
            self.speed = temp_speed
    

    def turn(self, direction, degrees):
        pass


class Truck(Vehicle):
    """Standard class for large motor vehicle"""
    def __init__(self, speed, desired_speed, direction, location, load_weight):
        super().__init__(speed, desired_speed, direction, location)
        self.load_weight = load_weight
    
    def accelerate(self, seconds):
        if (self.load_weight <= 5):
            temp_speed = self.speed + (Constants.ACC_RATE_EMPTY * seconds * Constants.MPS_TO_MPH)
        else:
            temp_speed = self.speed + (Constants.ACC_RATE_FULL * seconds * Constants.MPS_TO_MPH)
            
        if (temp_speed > self.desired_speed):
            self.speed = self.desired_speed
        else:
            self.speed = temp_speed

                
    def decelerate(self, seconds):
        if (self.load_weight <= 5):
            temp_speed = self.speed - (Constants.DEC_RATE_EMPTY * seconds * Constants.MPS_TO_MPH)
        else:
            temp_speed = self.speed - (Constants.DEC_RATE_FULL * seconds * Constants.MPS_TO_MPH)
            
        if (temp_speed < self.desired_speed):
            self.speed = self.desired_speed
        else:
            self.speed = temp_speed
    
    def turn(self, direction, degrees):
        pass
    