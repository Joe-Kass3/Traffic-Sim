"""
Mar 20 2022

Joe Kass
"""
from abc import ABC, abstractmethod
from Vehicle import Vehicle, Car, Truck
from Road import Road, Heading
from Map import Map
from Common import Constants
from Static_Road_Item import Stop_Sign, Speed_Limit_Sign
from Dynamic_Road_Item import Traffic_Light, Color
from Simulator import Simulation

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
            raise TypeError("{} is not a Vehicle object".format(type(vehicle)))
        return (vehicle.speed)
    
    def create_road(self, road_name, loc_x, loc_y, road_len, heading):
        return Road(road_name, loc_x / Constants.METERS_TO_MILES, loc_y / Constants.METERS_TO_MILES, road_len / Constants.METERS_TO_MILES, heading)

    def create_speed_limit(self, speed, distance):
        return Speed_Limit_Sign(speed, distance / Constants.METERS_TO_MILES)
    
    def create_stop_sign(self, distance):
        return Stop_Sign(distance / Constants.METERS_TO_MILES)
        
class MetricOutput(ISimOutput):
    """Metric Unit Conversion"""

    @property
    def _unit_name(self):
        return 'kph'
        
    def get_speed(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("{} is not a Vehicle object".format(type(vehicle)))
        return (vehicle.speed * 1.6)
    
    def create_road(self, road_name, loc_x, loc_y, road_len, heading):
        return Road(road_name, loc_x / Constants.METERS_TO_KM, loc_y / Constants.METERS_TO_KM, road_len / Constants.METERS_TO_KM, heading)

    def create_speed_limit(self, speed, distance):
        return Speed_Limit_Sign(speed, distance / Constants.METERS_TO_KM)
    
    def create_stop_sign(self, distance):
        return Stop_Sign(distance / Constants.METERS_TO_KM)


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
        
        #self.speed_limit = int(input("Enter speed limit: ")) #this will be changed, speed limit belongs attributed to road


if __name__ == "__main__":
    # gui = GUI()
    # mp = Map()
    # mp.load_map('test_map')
    
    sim = Simulation()
    
    light1 = Traffic_Light(7,2,5,Color.green,0.0)
    light2 = Traffic_Light(7,2,5,Color.red,0.0)
    
    sim.add_dynamic_object(light1)
    sim.add_dynamic_object(light2)
    
    for i in range(20):
        sim.update(1)
        print("Light 1: " + str(light1.current_color))
        print("Light 2: " + str(light2.current_color))
    
    # uptown = gui.output.create_road("Uptown", 0.0, -0.09, .180, Heading.North)
    # mp.add_road(uptown)
    # crosstown = gui.output.create_road("Crosstown", -0.09, 0.0, .180, Heading.East);
    # mp.add_road(crosstown)
    # sign1 = gui.output.create_stop_sign(0.01)
    # sign2 = gui.output.create_stop_sign(0.23)
    # sign3 = gui.output.create_stop_sign(0.32)
    # sign4 = gui.output.create_stop_sign(0.302)
    # limit1 = gui.output.create_speed_limit(80.0, 0.02)
    # limit2 = gui.output.create_speed_limit(50.0, 0.123)
    
    # uptown.add_item(sign2)
    # uptown.add_item(sign3)
    # uptown.add_item(sign4)
    # uptown.add_item(limit2)
    # crosstown.add_item(sign1)
    # crosstown.add_item(limit1)

    # mp.print_map()
    # mp.display_map()
    # mp.save_map('items_map')
    
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