'''
Created on 7 Mar 2018

@author: lauri
'''
from object import Object
from physics import Physics
from vector import Vector


'''
System class includes all objects in the simulation.
It updates every object's acceleration and checks collisions.
'''
class System():
    
    def __init__(self, dt):
        self.objects = []
        self.dt = dt
        self.collision = False
        
        self.counter = 0
        
    
    '''
    Get list of objects stored in system.
    '''
    def get_objects(self):
        return self.objects
    
    
    '''
    Adds new object to list in system.
    '''
    def new_object(self, obj):
        self.objects.append(obj)
        
    
    '''
    Returns dt.
    '''
    def get_dt(self):
        return self.dt
        
    
    '''
    Returns collision status (True/False)
    '''
    def get_collision(self):
        return self.collision
    
    
    '''
    Updates all objects in the system.
    '''
    def update_objects(self):
        for i in self.objects:
            force = Vector(0, 0, 0)
            for j in self.objects:
                if i != j:
                    force.add(Physics.Force(i, j))
                    if i.get_location().distance(j.get_location()) <= i.get_diameter()/2 + j.get_diameter()/2:
                        self.collision = True
                        self.dt = 0
                
            acceleration = Physics.acc(i, force)
            
            i.update(acceleration, self.dt)
            
            