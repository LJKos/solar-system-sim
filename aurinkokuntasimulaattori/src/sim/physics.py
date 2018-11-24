'''
Created on 7 Mar 2018

@author: lauri
'''
from vector import Vector


'''
Physics class holds calculations for gravitational force and acceleration.
'''
class Physics():
    
    '''
    Calculates gravitational force on object (center) that is caused by another object (reference).
    Returns force vector.
    '''
    @staticmethod
    def Force(center, reference):
        G = 6.67384 * (10 ** (-11))
        m1 = center.get_mass()
        m2 = reference.get_mass()
        
        r = center.get_location().distance(reference.get_location())
        
        f = G * ((m1 * m2) / (r ** 2))
        
        direction = center.get_location().direction(reference.get_location())
        
        force = direction.scalar_mult(f)
        
        return force
    
    
    '''
    Returns object's (obj) acceleration vector that is caused by force vector (force)
    '''
    @staticmethod
    def acc(obj, force):
        mass = obj.get_mass()
        acceleration = force.scalar_mult(mass ** (-1))
        
        return acceleration
        