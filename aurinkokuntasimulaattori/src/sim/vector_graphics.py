'''
Created on 19 Apr 2018

@author: lauri
'''

import math
from PyQt5 import QtWidgets, QtGui, QtCore
from object import Object
from vector import Vector


'''
VectorGraphics class creates an arrow for graphics.
It calculates arrows length and direction and updates them.
'''
class VectorGraphics(QtWidgets.QGraphicsPolygonItem):
    
    def __init__(self, obj, vector_type, perspective, center_obj, system):
        super(VectorGraphics, self).__init__()
        
        self.obj = obj
        self.vector_type = vector_type
        self.perspective = perspective
        self.system = system
        self.center_obj = center_obj
        self.length = 10
        
        brush = QtGui.QBrush(1)
        pen = QtGui.QPen()
        self.setPen(pen)
        self.setBrush(brush)
        
        self.draw_vector()
        
    
    '''
    Creates arrow for graphics.
    '''
    def draw_vector(self):
        
        arrow = QtGui.QPolygonF()
        arrow.append(QtCore.QPointF(0, 0))
        arrow.append(QtCore.QPointF(0.5, 0))
        arrow.append(QtCore.QPointF(0.5, self.length-3))
        arrow.append(QtCore.QPointF(2, self.length-3))
        arrow.append(QtCore.QPointF(0, self.length))
        arrow.append(QtCore.QPointF(-2, self.length-3))
        arrow.append(QtCore.QPointF(-0.5, self.length-3))
        arrow.append(QtCore.QPointF(-0.5, 0))
        arrow.append(QtCore.QPointF(0, 0))
        self.setPolygon(arrow)
        
        if self.vector_type == 'acceleration':
            self.setPen(QtGui.QColor(100, 100, 250))
            self.setBrush(QtGui.QColor(100, 100, 250))
        elif self.vector_type == 'velocity':
            self.setPen(QtGui.QColor(255, 255, 50))
            self.setBrush(QtGui.QColor(255, 255, 50))
        
        
    '''
    Updates graphic objects position on screen.
    '''
    def update_vectors(self, scale_location, perspective, center_obj):
        self.scale_location = scale_location
        self.perspective = perspective
        self.center = center_obj.get_location().get_values()
        
        if self.vector_type == 'acceleration':
            self.length = 20 + math.log(self.obj.get_acceleration().length() * 2)
        elif self.vector_type == 'velocity':
            self.length = 10 + self.obj.get_velocity().length() / 5000
        
        self.draw_vector()
        
        location = self.obj.get_location().get_values()
        rad = 0
        angle = 0
        acc = self.obj.get_acceleration().get_values()
        vel = self.obj.get_velocity().get_values()
        
        if perspective == 'z':
            self.x = (location[0] - self.center[0]) * self.scale_location + 450
            self.y = (location[1] - self.center[1]) * self.scale_location + 200
            if self.vector_type == 'acceleration' and acc[1] != 0 and acc[0] != 0:
                rad = math.atan(acc[1] / acc[0])
                if acc[0] < 0:
                    angle = 180 + ((180 * rad) / math.pi) - 90
                else:
                    angle = ((180 * rad) / math.pi) - 90
                
            elif (self.vector_type == 'velocity') and (vel[1] != 0) and (vel[0] != 0):
                rad = math.atan(vel[1] / vel[0])
                if vel[0] < 0:
                    angle = 180 + ((180 * rad) / math.pi) - 90
                else:
                    angle = ((180 * rad) / math.pi) - 90
                
        else:
            self.x = (location[0] - self.center[0]) * self.scale_location + 450
            self.y = (location[2] - self.center[2]) * self.scale_location + 200
            if self.vector_type == 'acceleration' and acc[2] != 0 and acc[0] != 0:
                rad = math.atan(acc[2] / acc[0])
                if acc[0] < 0:
                    angle = 180 + ((180 * rad) / math.pi) - 90
                else:
                    angle = ((180 * rad) / math.pi) - 90
            
            elif (self.vector_type == 'velocity') and (vel[2] != 0) and (vel[0] != 0):
                rad = math.atan(vel[2] / vel[0])
                if vel[0] < 0:
                    angle = 180 + ((180 * rad) / math.pi) - 90
                else:
                    angle = ((180 * rad) / math.pi) - 90
            
            
        self.setPos(self.x, self.y)
        self.setRotation(angle)
    
    
    