"""
Mar 20 2022

Joe Kass
"""
from abc import ABC, abstractmethod
from Vehicle import Vehicle, Car, Truck
from Road import Road, Heading
from Map import Map
from Common import Constants

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
    
    def create_road(self, road_name, loc_x, loc_y, road_len, heading):
        return Road(road_name, loc_x / Constants.METERS_TO_MILES, loc_y / Constants.METERS_TO_MILES, road_len / Constants.METERS_TO_MILES, heading)

        
class MetricOutput(ISimOutput):
    """Metric Unit Conversion"""

    @property
    def _unit_name(self):
        return 'kph'
        
    def get_speed(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("{} is not a Vehicle class".format(type(vehicle)))
        return (vehicle.speed * 1.6)
    
    def create_road(self, road_name, loc_x, loc_y, road_len, heading):

        return Road(road_name, loc_x / Constants.METERS_TO_KM, loc_y / Constants.METERS_TO_KM, road_len / Constants.METERS_TO_KM, heading)

class GUI:
    """GUI Class for the program"""
    def __init__(self):
        self.unit = input("Enter 'M' for Metric or 'I' for Imperial: ")
        
        if (self.unit == "M"):
            self.output = MetricOutput()
        elif (self.unit == "I"):
            self.output = ImperialOutput()
        else:
            raise ValueError("Choice of unit must be 'M' or 'I'")
        
        self.speed_limit = int(input("Enter speed limit: ")) #this will be changed


if __name__ == "__main__":
    gui = GUI()
    mp = Map()
    uptown = gui.output.create_road("Uptown", 0.0, -0.09, .180, Heading.North)
    mp.add_road(uptown)
    crosstown = gui.output.create_road("Crosstown", -0.09, 0.0, .180, Heading.East);
    mp.add_road(crosstown)
    #print(mp._list_roads)
    
    mp.print_map()
    mp.display_map()
    
    
    # car = Car(0, gui.speed_limit, 0, 0)
    # truck1 = Truck(0, gui.speed_limit, 0, 1, 4)
    # truck2 = Truck(0, gui.speed_limit, 0, 2, 8)
    # v_list = [car, truck1, truck2]
    # #output = ImperialOutput()
    # #output = MetricOutput()
    
    # for i in range(11):
    #     for j in range(len(v_list)):
    #         v_list[j].update_speed(1)
    #         print('{0} speed: {1:8.2f} {2}'.format(type(v_list[j]).__name__, gui.output.get_speed(v_list[j]), gui.output._unit_name))