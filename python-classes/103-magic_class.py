#!/usr/bin/python3
"""
magic class.
"""
class MagicClass:
    def __init__(self, radius=0):
        self.__radius = radius
    
    def area_of_circle(self):
        return math.pi * self.__radius ** 2
    
    def circumference_of_circle(self):
        return 2 * math.pi * self.__radius

