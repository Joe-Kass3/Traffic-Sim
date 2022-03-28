"""
Mar 20 2022

Joe Kass
"""
 
from Common import Conversions, Constants

class Char_Matrix:
    """character representation of the map"""
    def __init__(self, matrix_size = Constants.CHAR_MAP_SIZE):
        self.char_map = [[' ']*matrix_size for _ in range(matrix_size)]

class Console_Print:
    
    def print_road(cm, road):
        """display road in current char matrix"""
        CC_x = Conversions.WC_point_to_CC_point(road.loc_x)
        CC_y = Conversions.WC_point_to_CC_point(road.loc_y)
        CC_length = Conversions.WC_length_to_CC_length(road.length)
        road_dist = 0

        #match available in py 3.10
        if road.heading.name == 'North':
            x = CC_x
            if (x >= 0 and x < Constants.CHAR_MAP_SIZE):
                while (road_dist < CC_length):
                    y = CC_y - road_dist
                    if (y>=0 and y < Constants.CHAR_MAP_SIZE):
                        cm.char_map[y][x] = '|'
                        cm.char_map[y][x + 2] = '|'
                        cm.char_map[y][x + 4] = '|'
                    road_dist += 1
            
        elif road.heading.name == 'South':
            pass
        elif road.heading.name == 'East':
            y = CC_y
            if (y >= 0 and y < Constants.CHAR_MAP_SIZE):
                while (road_dist < CC_length):
                    x = CC_x - road_dist
                    if (x>=0 and x < Constants.CHAR_MAP_SIZE):

                        cm.char_map[y][x] = '-'
                        cm.char_map[y + 2][x] = '-'
                        cm.char_map[y + 4][x] = '-'
                    
                    road_dist += 1  
                    
        elif road.heading.name == 'West':
            pass

    def print_car(cm, car):
        pass

