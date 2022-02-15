"""
Wed Jan 19 2022

Joe Kass
"""

from abc import ABC, abstractmethod

# Define Constants
ACC_RATE = 3.5              # Acceleration rate for cars in m/s
ACC_RATE_EMPTY = 2.5        # Acceleration rate for light trucks in m/s
ACC_RATE_FULL = 1.0         # Acceleration rate for heavy trucks in m/s
DEC_RATE = 7.0              # Braking rate for cars in m/s
DEC_RATE_EMPTY = 5.0        # Braking rate for light trucks in m/s
DEC_RATE_FULL = 2.0         # Braking rate for light trucks in m/s
MPS_TO_MPH = 2.237

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
        temp_speed = self.speed + (ACC_RATE * seconds * MPS_TO_MPH)
        if (temp_speed > self.desired_speed):
            self.speed = self.desired_speed
        else:
            self.speed = temp_speed

    def decelerate(self, seconds):
        temp_speed = self.speed - (DEC_RATE * seconds * MPS_TO_MPH)
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
    
# Disabled for timebeing, will remove entirely unless there is some need for control of setting load weight
#    def set_load_weight(self, weight):
#        self.load_weight = weight
    
    def accelerate(self, seconds):
        if (self.load_weight <= 5):
            temp_speed = self.speed + (ACC_RATE_EMPTY * seconds * MPS_TO_MPH)
        else:
            temp_speed = self.speed + (ACC_RATE_FULL * seconds * MPS_TO_MPH)
            
        if (temp_speed > self.desired_speed):
            self.speed = self.desired_speed
        else:
            self.speed = temp_speed

                
    def decelerate(self, seconds):
        if (self.load_weight <= 5):
            temp_speed = self.speed - (DEC_RATE_EMPTY * seconds * MPS_TO_MPH)
        else:
            temp_speed = self.speed - (DEC_RATE_FULL * seconds * MPS_TO_MPH)
            
        if (temp_speed < self.desired_speed):
            self.speed = self.desired_speed
        else:
            self.speed = temp_speed
    
    def turn(self, direction, degrees):
        pass
    
    
class ISimOutput(ABC):
    """Base class for vehicle interface"""
    
    @property
    @abstractmethod
    def _unit_name(self):
        ...
    
    @abstractmethod
    def get_speed(self):
        ...
    
class ImperialOutput(ISimOutput):
    """Imperial Unit Conversion"""
    
    @property
    def _unit_name(self):
        return 'mph'
    
    def get_speed(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("{} is not a Vehicle class".format(type(vehicle)))
        return (vehicle.speed)
        
class MetricOutput(ISimOutput):
    """Metric Unit Conversion"""

    @property
    def _unit_name(self):
        return 'kph'
        
    def get_speed(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("{} is not a Vehicle class".format(type(vehicle)))
        return (vehicle.speed * 1.6)
    
    
if __name__ == "__main__":
    car = Car(0, 65, 0, 0)
    truck1 = Truck(0, 55, 0, 1, 4)
    truck2 = Truck(0, 50, 0, 2, 8)
    v_list = [car, truck1, truck2]
    #output = ImperialOutput()
    output = MetricOutput()
    
    for i in range(11):
        for j in range(len(v_list)):
            v_list[j].update_speed(1)
            print('{0} speed: {1:8.2f} {2}'.format(type(v_list[j]).__name__, output.get_speed(v_list[j]), output._unit_name))
        
