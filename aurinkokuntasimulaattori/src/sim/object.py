'''
Created on 7 Mar 2018

@author: lauri
'''
import math
from vector import Vector


'''
Object class creates objects for the system.
Every object gets graphics from ObjectGraphics class.
'''
class Object():
    
    def __init__(self, name, location, velocity, mass, density):
        self.name = name
        self.location = Vector(location[0], location[1], location[2])
        self.velocity = Vector(velocity[0], velocity[1], velocity[2])
        self.acceleration = Vector(0, 0, 0)
        self.mass = mass
        self.density = density
        
    
    '''
    Returns the name of the object.
    '''
    def get_name(self):
        return self.name
       
    
    '''
    Returns the mass of the object.
    '''
    def get_mass(self):
        return self.mass
    
    
    '''
    Returns the density of the object.
    '''
    def get_density(self):
        return self.density
    
    
    '''
    Returns the diameter of the object.
    '''
    def get_diameter(self):
        volume = self.mass / self.density
        diameter = 2 * (((3 * volume) / (4 * math.pi)) ** (1 / 3))
        
        return diameter
    
    
    '''
    Returns the location vector of the object.
    '''
    def get_location(self):
        return self.location
    
    
    '''
    Returns the velocity vector of the object.
    '''
    def get_velocity(self):
        return self.velocity
    
    
    '''
    Returns the acceleration vector of the object.
    '''
    def get_acceleration(self):
        return self.acceleration
    
    
    '''
    Updates object's location with acceleration and velocity.
    '''
    def update(self, acceleration, dt):
        self.acceleration = acceleration
        self.velocity.add(self.acceleration.scalar_mult(dt))
        self.location.add(self.velocity.scalar_mult(dt))
        