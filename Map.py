"""
Sun Jan 30 2022

Joe Kass
"""

from Road import Road, Heading
from SUI import Console_Print, Char_Matrix
import json
from pathlib import Path
from Static_Road_Item import *
#from GUI import *

class Map:
    """Create Map for objects in Traffic Sim"""
    
    def __init__(self):
        self._list_roads = []
        self.cm = Char_Matrix()
    
    def add_road(self, road):
        """include new road in map object"""
        if not isinstance(road, Road):
            raise TypeError("{} is not of type Road ".format(type(road)))
        
        self._list_roads.append(road)
    
    def load_map(self, map_name):
        """ Add all roads in json representation of map. Will delete all current roads
            searches for named json file in ./maps/
        """
        self._list_roads = [] #delete current roads in map
        
        wd = Path().absolute()
        map_file = str(wd) + '\\maps\\' + map_name + '.json'

        data = json.load(open(map_file, 'r'))
        for road in data['Roads']:
            new_road = Road(road['Name'], road['XLocation'], road['YLocation'], road['Length'], Heading(road['Heading']))
            try:
                for item in road['RoadItems']:
                    if (item['Type'] == 'StopSign'):
                        road_item = Stop_Sign(item['MileMarker'])
                    if (item['Type'] == 'SpeedLimit'):
                        road_item = Speed_Limit_Sign(item['SpeedLimit'], item['MileMarker'])
                    
                    new_road.add_item(road_item)
            except KeyError:
                ...
            
            self._list_roads.append(new_road)
            print('here')

    def save_map(self, map_name):
        """ Save map as json representation. file placed in ./maps/ folder"""
        data = {}
        roads = []
        
        wd = Path().absolute()
        map_file = str(wd) + '\\maps\\' + map_name + '.json'
        
        for road in self._list_roads:
            road_items = []
            for item in road._items:
                if isinstance(item, Stop_Sign):
                    road_items.append({"Type":"StopSign","MileMarker":item.mile_marker})
                if isinstance(item, Speed_Limit_Sign):
                    road_items.append({"Type":"SpeedLimit","MileMarker":item.mile_marker,"SpeedLimit":item.posted_speed})
            roads.append({"Name":road.name,"Length":road.length,"XLocation":road.loc_x,"YLocation":road.loc_y,"Heading":road.heading.value,
                          "RoadItems":road_items})
        
        data['Roads'] = roads

        with open(map_file, 'w') as f:
            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        
    def print_map(self):
        """Print the map as provided"""
        for road in self._list_roads:
            Console_Print.print_road(self.cm, road)
            
    def display_map(self):
        """show the map in console"""
        for row in self.cm.char_map:
            for col in row:
                print(col, end="") 
            print()