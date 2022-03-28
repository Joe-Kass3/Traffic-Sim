"""
Mar 20 2022

Joe Kass
"""
from Vehicle import GUI, Car, Truck
from Road import Road, Heading
from Map import Map


if __name__ == "__main__":
    #gui = GUI()
    mp = Map()
    uptown = Road("Uptown", 0.0, -0.09, 180, Heading.North)
    mp.add_road(uptown)
    crosstown = Road("Crosstown", -0.09, 0.0, 180, Heading.East);
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