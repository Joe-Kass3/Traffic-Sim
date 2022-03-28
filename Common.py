"""
Mar 20 2022

Joe Kass
"""

class Constants:
    """Class with constants used throughout"""
    ACC_RATE = 3.5              # Acceleration rate for cars in m/s
    ACC_RATE_EMPTY = 2.5        # Acceleration rate for light trucks in m/s
    ACC_RATE_FULL = 1.0         # Acceleration rate for heavy trucks in m/s
    DEC_RATE = 7.0              # Braking rate for cars in m/s
    DEC_RATE_EMPTY = 5.0        # Braking rate for light trucks in m/s
    DEC_RATE_FULL = 2.0         # Braking rate for light trucks in m/s
    MPS_TO_MPH = 2.237
    MPS_TO_KPH = 3.6
    METERS_TO_MILES = 0.000621371
    METERS_TO_KM = 0.001
    CHAR_MAP_SIZE = 40
    WORLD_SIZE = 200.0

class Conversions(object):
    """Handle conversion of display sizing"""

    @staticmethod
    def WC_point_to_CC_point(val):
        return(int(val * (Constants.CHAR_MAP_SIZE / Constants.WORLD_SIZE) + (Constants.CHAR_MAP_SIZE / 2)))
        
    @staticmethod
    def WC_length_to_CC_length(val):
        return(int(val * (Constants.CHAR_MAP_SIZE / Constants.WORLD_SIZE)))