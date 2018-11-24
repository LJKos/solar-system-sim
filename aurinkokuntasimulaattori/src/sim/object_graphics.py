'''
Created on 12 Mar 2018

@author: lauri
'''

from PyQt5 import QtWidgets, QtGui
from object import Object
from vector import Vector
from PyQt5.Qt import QRectF


'''
ObjectGraphics class creates an ellipse to the screen for every object.
Position is read from object.
'''
class ObjectGraphics(QtWidgets.QGraphicsEllipseItem):
    
    def __init__(self, obj, scale_size, scale_location, scale_size_diff, perspective, center_obj, system):
        super(ObjectGraphics, self).__init__()
        
        self.obj = obj
        self.scale_size = scale_size
        self.scale_location = scale_location
        self.scale_size_diff = scale_size_diff
        self.perspective = perspective
        self.system = system
        self.center_obj = center_obj
        self.x = 0
        self.y = 0
        
        brush = QtGui.QBrush(1)
        self.setBrush(brush)
        
        self.draw_object()
        
    
    '''
    Creates ellipse for graphics.
    '''
    def draw_object(self):
        object_graphics = QRectF(0, 0, self.obj.get_diameter(), self.obj.get_diameter())
        self.setRect(object_graphics)
        self.setTransformOriginPoint(self.obj.get_diameter() / 2, self.obj.get_diameter() / 2)
        self.setBrush(QtGui.QBrush(QtGui.QColor(250, 250, 250)))
        
    
    '''
    Updates graphic objects position on screen.
    '''
    def update(self, perspective, scale_size, scale_location, scale_size_diff, center_obj):
        location = self.obj.get_location().get_values()
        self.perspective = perspective
        self.scale_size = scale_size
        self.scale_location = scale_location
        self.scale_size_diff = scale_size_diff
        self.center = center_obj.get_location().get_values()
        
        if perspective == 'z':
            self.x = (location[0] - self.center[0]) * self.scale_location - (self.obj.get_diameter() / 2) + 450
            self.y = (location[1] - self.center[1]) * self.scale_location - (self.obj.get_diameter() / 2) + 200
        else:
            self.x = (location[0] - self.center[0]) * self.scale_location - (self.obj.get_diameter() / 2) + 450
            self.y = (location[2] - self.center[2]) * self.scale_location - (self.obj.get_diameter() / 2) + 200
            
        self.setPos(self.x, self.y)
        self.setScale(self.scale_size)
        
        