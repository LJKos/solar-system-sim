'''
Created on 7 Mar 2018

@author: lauri
'''
import math


'''
Vector class creates three dimensional vector object that is used for calculations.
There are operations for vector calculation.
'''
class Vector():
    
    
    '''
    Creates new three dimensional vector (x, y, z).
    '''
    def __init__(self, value1, value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.vector = [value1, value2, value3]
        
    
    '''
    Returns values stored in vector.
    '''
    def get_values(self):
        return [self.value1, self.value2, self.value3]
    
    
    '''
    Adds given vector (vector).
    (vector1.add(vector2))
    '''
    def add(self, vector):
        self.value1 += vector.get_values()[0]
        self.value2 += vector.get_values()[1]
        self.value3 += vector.get_values()[2]
    
    
    '''
    Returns distance of two points (vectors).
    (distance = vector1.distance(vector2))
    '''
    def distance(self, vector):
        distance = math.sqrt((vector.get_values()[0] - self.value1) ** 2 + (vector.get_values()[1] - self.value2) ** 2 + (vector.get_values()[2] - self.value3) ** 2)
        
        return distance
    
    
    '''
    Returns unit vector.
    (new_vector = vector.unit())
    '''
    def unit(self):
        length = math.sqrt(self.value1 ** 2 + self.value2 ** 2 + self.value3 ** 2)
        vector = Vector(self.value1 / length, self.value2 / length, self.value3 / length)
        
        return vector
    
    
    '''
    Returns the length of the vector.
    '''
    def length(self):
        length = math.sqrt(self.value1 ** 2 + self.value2 ** 2 + self.value3 ** 2)
        
        return length
    
    
    '''
    Multiplies every component of vector with given value.
    (new_vector = vector.to_components(value))
    '''
    def scalar_mult(self, value):
        vector = Vector(value * self.value1, value * self.value2, value * self.value3)
        
        return vector
    
    
    '''
    Returns unit vector that shows direction to given vector.
    (new_vector = vector1.direction(vector2))
    '''
    def direction(self, vector):
        subs = Vector(vector.get_values()[0] - self.value1, vector.get_values()[1] - self.value2, vector.get_values()[2] - self.value3)
        vector = subs.unit()
        
        return vector
        
        
        