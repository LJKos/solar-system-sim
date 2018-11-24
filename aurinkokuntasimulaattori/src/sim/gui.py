'''
Created on 7 Mar 2018

@author: lauri
'''

from object import Object
from system import System
from file_reader import FileReader
from PyQt5 import QtWidgets, QtCore, QtGui
from object_graphics import ObjectGraphics
from vector_graphics import VectorGraphics


'''
GUI class creates the graphical user interface.
It has 50Hz update rate for graphics and it also defines update rate for objects' physics.
'''
class GUI(QtWidgets.QMainWindow):
    
    def __init__(self, system):
        super().__init__()
        
        self.system = system
        self.perspective = 'z'
        self.scale_size = 2.0348488538587373e-07
        self.scale_location = 2.352492818225932e-09
        self.scale_size_diff = 0
        self.time_counter = 0
        self.time = 0
        self.center_obj = self.system.get_objects()[0]
        self.added_objects = []
        self.added_vectors = []
        self.hide_vectors = False
        self.data_string = ''
        
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        
        self.title = 'Solar System Simulation'
        self.top = 0
        self.left = 0
        self.width = 900
        self.height = 600
        self.store_dt = self.system.dt
        self.system.dt = 0
        
        '''
        Calls functions that have to be called once.
        '''
        self.init_window()
        self.init_buttons()
        self.add_objects_to_scene()
        self.update_objects()
        
        '''
        Creates timer that defines how often graphics are updated.
        '''
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_objects)
        '''
        50Hz refresh
        '''
        self.timer.start(20)
        
        
    def init_window(self):
        '''
        Initializes window for graphics.
        '''
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(self.left, self.top, self.width, self.height * (2 / 3))
        self.scene.setBackgroundBrush(QtGui.QColor(0, 0, 20))
        
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        '''
        QLabels for texts:
        '''
        '''
        Text for scaling size and distance.
        '''
        self.scale = QtWidgets.QLabel(self)
        self.scale.move((self.width / 6) * 0.5, self.height / 1.5)
        self.scale.setText('Scale:')
        
        '''
        Text for changing object in the center of the screen.
        '''
        self.next_center = QtWidgets.QLabel(self)
        self.next_center.move((self.width / 6) * 2, self.height / 1.5)
        self.next_center.setText('Center object:')
        
        '''
        Text for setting time span.
        '''
        self.set_time_span_text = QtWidgets.QLabel(self)
        self.set_time_span_text.move((self.width / 6) * 3.5-40, self.height / 1.5)
        self.set_time_span_text.setFixedWidth(200)
        self.set_time_span_text.setText('Set time span: (s)')
        
        '''
        Text for changing dt.
        '''
        self.change_dt = QtWidgets.QLabel(self)
        self.change_dt.move((self.width / 6) * 5, self.height / 1.5)
        self.change_dt.setText('Change dt:')
        
        '''
        Text for value error.
        '''
        self.value_error = QtWidgets.QLabel(self)
        self.value_error.move((self.width / 6) * 5.4, self.height / 1.1)
        self.value_error.setStyleSheet("QLabel {color : red; font : 11pt}")
        self.value_error.setText('Value error!')
        self.value_error.hide()
        
        '''
        Initializing collision text.
        '''
        self.collision = QtWidgets.QLabel(self)
        self.collision.move(20, self.height / 1.6)
        self.collision.setStyleSheet("QLabel {color : white; font : 11pt}")
        self.collision.setText('Collision: ' + str(self.system.get_collision()))
        
        '''
        Frame rate text.
        '''
        self.frame_rate = QtWidgets.QLabel(self)
        self.frame_rate.move(120, self.height / 1.6)
        self.frame_rate.setStyleSheet("QLabel {color : white; font : 11pt}")
        self.frame_rate.setText('Frame rate: 50Hz')
        
        '''
        Initializing time step text.
        '''
        self.time_step = QtWidgets.QLabel(self)
        self.time_step.move(240, self.height / 1.6)
        self.time_step.setStyleSheet("QLabel {color : white; font : 11pt}")
        self.time_step.setText('dt: ' + str(self.system.get_dt()) + ' s')
        
        '''
        Initializing simulation speed text.
        '''
        self.simulation_speed = QtWidgets.QLabel(self)
        self.simulation_speed.move(330, self.height / 1.6)
        self.simulation_speed.setFixedWidth(200)
        self.simulation_speed.setStyleSheet("QLabel {color : white; font : 11pt}")
        self.simulation_speed.setText('Real time x ')
        
        '''
        Initializing time span text.
        '''
        self.time_span = QtWidgets.QLabel(self)
        self.time_span.move(460, self.height / 1.6)
        self.time_span.setFixedWidth(160)
        self.time_span.setStyleSheet("QLabel {color : white; font : 11pt}")
        self.time_span.setText('Time span: ')
        
        '''
        Initializing size to distance ratio text.
        '''
        self.size_to_distance = QtWidgets.QLabel(self)
        self.size_to_distance.move(620, self.height / 1.6)
        self.size_to_distance.setFixedWidth(200)
        self.size_to_distance.setStyleSheet("QLabel {color : white; font : 11pt}")
        self.size_to_distance.setText('size to distance ratio: ')
        
        '''
        Text for adding new object's name.
        '''
        self.add_name = QtWidgets.QLabel(self)
        self.add_name.move((self.width / 7) * 0.5, self.height / 1.15)
        self.add_name.setText('Name:')
        
        '''
        Text for adding new object's location.
        '''
        self.add_location = QtWidgets.QLabel(self)
        self.add_location.move((self.width / 7) * 1.5, self.height / 1.15)
        self.add_location.setFixedWidth(200)
        self.add_location.setText('Location: (m,...,...)')
        
        '''
        Text for adding new object's velocity.
        '''
        self.add_velocity = QtWidgets.QLabel(self)
        self.add_velocity.move((self.width / 7) * 2.5, self.height / 1.15)
        self.add_velocity.setFixedWidth(200)
        self.add_velocity.setText('Velocity: (m/s,...,...)')
        
        '''
        Text for adding new object's mass.
        '''
        self.add_mass = QtWidgets.QLabel(self)
        self.add_mass.move((self.width / 7) * 3.5, self.height / 1.15)
        self.add_mass.setText('Mass: (kg)')
        
        '''
        Text for adding new object's density.
        '''
        self.add_density = QtWidgets.QLabel(self)
        self.add_density.move((self.width / 7) * 4.5, self.height / 1.15)
        self.add_density.setFixedWidth(200)
        self.add_density.setText('Density: (kg/m^3)')
        
        '''
        Text for the center object's name.
        '''
        self.center_name = QtWidgets.QLabel(self)
        self.center_name.setStyleSheet("QLabel {color : white; font : 11pt}")
        self.center_name.move(20, 20)
        self.center_name.setFixedWidth(500)
        self.center_name.setFixedHeight(12)
        
        '''
        Text for the center object's location.
        '''
        self.center_location = QtWidgets.QLabel(self)
        self.center_location.setStyleSheet("QLabel {color : white; font : 10pt}")
        self.center_location.move(20, 30)
        self.center_location.setFixedWidth(600)
        self.center_location.setFixedHeight(12)
        
        '''
        Text for the center object's velocity.
        '''
        self.center_velocity = QtWidgets.QLabel(self)
        self.center_velocity.setStyleSheet("QLabel {color : white; font : 10pt}")
        self.center_velocity.move(20, 40)
        self.center_velocity.setFixedWidth(300)
        self.center_velocity.setFixedHeight(12)
        
        '''
        Text for the center object's acceleration.
        '''
        self.center_acceleration = QtWidgets.QLabel(self)
        self.center_acceleration.setStyleSheet("QLabel {color : white; font : 10pt}")
        self.center_acceleration.move(20, 50)
        self.center_acceleration.setFixedWidth(300)
        self.center_acceleration.setFixedHeight(12)
        
        '''
        Text for the center object's mass.
        '''
        self.center_mass = QtWidgets.QLabel(self)
        self.center_mass.setStyleSheet("QLabel {color : white; font : 10pt}")
        self.center_mass.move(20, 60)
        self.center_mass.setFixedWidth(300)
        self.center_mass.setFixedHeight(12)
        
        '''
        Text for the center object's density.
        '''
        self.center_density = QtWidgets.QLabel(self)
        self.center_density.setStyleSheet("QLabel {color : white; font : 10pt}")
        self.center_density.move(20, 70)
        self.center_density.setFixedWidth(300)
        self.center_density.setFixedHeight(12)
        
    '''
    Initializes every button on the screen.
    Called once when gui is defined.
    '''
    def init_buttons(self):
        
        '''
        Scale size of objects
        '''
        self.size_m = QtWidgets.QPushButton('size: -', self)
        self.size_m.move((self.width / 6) * 0.5-50, self.height / 1.4)
        self.size_m.clicked.connect(self.scale_size_m)
        
        self.size_p = QtWidgets.QPushButton('size: +', self)
        self.size_p.move((self.width / 6) * 0.5+50, self.height / 1.4)
        self.size_p.clicked.connect(self.scale_size_p)
        
        '''
        Scale distances between objects
        '''
        self.location_m = QtWidgets.QPushButton('distance: -', self)
        self.location_m.move((self.width / 6) * 0.5-50, self.height / 1.32)
        self.location_m.clicked.connect(self.scale_location_m)
        
        self.location_p = QtWidgets.QPushButton('distance: +', self)
        self.location_p.move((self.width / 6) * 0.5+50, self.height / 1.32)
        self.location_p.clicked.connect(self.scale_location_p)
        
        '''
        Scale distance to size
        '''
        self.dist_to_size = QtWidgets.QPushButton('dist. to size', self)
        self.dist_to_size.move((self.width / 6) * 0.5-50, self.height / 1.24)
        self.dist_to_size.clicked.connect(self.scale_dist_to_size)
        
        '''
        Change perspective
        '''
        self.persp = QtWidgets.QPushButton('perspective', self)
        self.persp.move((self.width / 6) * 0.5+50, self.height / 1.24)
        self.persp.clicked.connect(self.change_perspective)
        
        '''
        Pause
        '''
        self.persp = QtWidgets.QPushButton('pause', self)
        self.persp.move((self.width / 6) * 5, self.height / 1.32)
        self.persp.clicked.connect(self.pause)
        
        '''
        Change dt
        '''
        self.dt_m = QtWidgets.QPushButton('dt: -', self)
        self.dt_m.move((self.width / 6) * 5-50, self.height / 1.4)
        self.dt_m.clicked.connect(self.change_dt_m)
        
        self.dt_p = QtWidgets.QPushButton('dt: +', self)
        self.dt_p.move((self.width / 6) * 5+50, self.height / 1.4)
        self.dt_p.clicked.connect(self.change_dt_p)
        
        '''
        Add objects to simulation
        '''
        self.add = QtWidgets.QPushButton('add object', self)
        self.add.move((self.width / 7) * 5.5, self.height / 1.1)
        self.add.clicked.connect(self.new_object_to_scene)
        
        self.name_edit = QtWidgets.QLineEdit(self)
        self.name_edit.move((self.width / 7) * 0.5, self.height / 1.1)
        
        self.location_edit = QtWidgets.QLineEdit(self)
        self.location_edit.move((self.width / 7) * 1.5, self.height / 1.1)
        
        self.velocity_edit = QtWidgets.QLineEdit(self)
        self.velocity_edit.move((self.width / 7) * 2.5, self.height / 1.1)
        
        self.mass_edit = QtWidgets.QLineEdit(self)
        self.mass_edit.move((self.width / 7) * 3.5, self.height / 1.1)
        
        self.density_edit = QtWidgets.QLineEdit(self)
        self.density_edit.move((self.width / 7) * 4.5, self.height / 1.1)
        
        '''
        Change object in the center
        '''
        self.center_obj_m = QtWidgets.QPushButton('center: -', self)
        self.center_obj_m.move((self.width / 6) * 2-50, self.height / 1.4)
        self.center_obj_m.clicked.connect(self.center_object_m)
        
        self.center_obj_p = QtWidgets.QPushButton('center: +', self)
        self.center_obj_p.move((self.width / 6) * 2+50, self.height / 1.4)
        self.center_obj_p.clicked.connect(self.center_object_p)
        
        '''
        Hide vectors
        '''
        self.hide_v = QtWidgets.QPushButton('vectors', self)
        self.hide_v.move((self.width / 6) * 2-50, self.height / 1.24)
        self.hide_v.clicked.connect(self.hide_vector)
        
        '''
        Hide vectors
        '''
        self.save = QtWidgets.QPushButton('save', self)
        self.save.move((self.width / 6) * 2+50, self.height / 1.24)
        self.save.clicked.connect(self.save_data)
        
        '''
        Set time span
        '''
        self.set_time_span = QtWidgets.QPushButton('set', self)
        self.set_time_span.move((self.width / 7) * 4+50, self.height / 1.4)
        self.set_time_span.clicked.connect(self.set_t)
        
        self.time_span_edit = QtWidgets.QLineEdit(self)
        self.time_span_edit.move((self.width / 7) * 4-50, self.height / 1.4)
        
    
    '''
    Goes through objects in the system and adds graphics (ObjectGraphics).
    This is function will run only once when gui is defined.
    ''' 
    def add_objects_to_scene(self):
        for i in range(len(self.system.get_objects())):
            objects = System.get_objects(self.system)
            obj = ObjectGraphics(objects[i], self.scale_size, self.scale_location, self.scale_size_diff, self.perspective, self.center_obj, self.system)
            acc = VectorGraphics(objects[i], 'acceleration', self.perspective, self.center_obj, self.system)
            vel = VectorGraphics(objects[i], 'velocity', self.perspective, self.center_obj, self.system)

            if obj not in self.added_objects:
                self.scene.addItem(acc)
                self.scene.addItem(vel)
                self.scene.addItem(obj)
                self.added_objects.append(obj)
                self.added_vectors.append(acc)
                self.added_vectors.append(vel)
    
    
    '''
    Updates graphics in the scene and checks collisions.
    '''
    def update_objects(self):
        self.system.update_objects()
        for i in self.added_objects:
            i.update(self.perspective, self.scale_size, self.scale_location, self.scale_size_diff, self.center_obj)
        
        for i in self.added_vectors:
            i.update_vectors(self.scale_location, self.perspective, self.center_obj)
            if self.hide_vectors:
                i.hide()
            else:
                i.setVisible(True)
        
        self.collision_status()
        self.dt()
        self.sim_speed()
        self.size_to_dist()
        self.t()
        self.object_info(self.center_obj)
        self.show()
    
    
    '''
    Changes perspective of the screen (looking from up or side).
    '''
    def change_perspective(self):
        if self.perspective == 'z':
            self.perspective = 'y'
        else:
            self.perspective = 'z'
    

    '''
    Shows collision status for the user (False/True).
    '''
    def collision_status(self):
        self.collision.setText('Collision: ' + str(self.system.get_collision()))
        
    
    '''
    Shows the length of the time step.
    '''
    def dt(self):
        self.time_step.setText('dt: ' + str(self.system.get_dt()) + ' s')
        
    
    '''
    Shows simulation speed.
    '''
    def sim_speed(self):
        self.simulation_speed.setText('Real time x ' + str(self.system.get_dt() * 50))
    
    
    '''
    Time span
    '''
    def set_t(self):
        try:
            self.time = int(self.time_span_edit.text())
            self.value_error.hide()
            
        except ValueError:
            self.value_error.setVisible(True)
    
    
    '''
    Time span
    '''
    def t(self):
        if self.system.dt != 0:
            if self.time != 0:
                self.time_counter += 1
            if self.time_counter % 50 == 0 and self.time > 0:
                self.time -= 50 * self.system.dt
            elif self.time_counter != 0 and self.time <= 0:
                self.store_dt = self.system.dt
                self.system.dt = 0
                self.time_counter = 0
            
        self.time_span.setText('Time span: ' + str(self.time) + ' s')
        
    
    '''
    Shows ratio between size and distance.
    '''
    def size_to_dist(self):
        self.size_to_distance.setText('size to distance ratio: ' + str(round(self.scale_size / self.scale_location, 5)))
        
    
    '''
    Shows information about the object that is selected to the center.
    '''
    def object_info(self, center_obj):
        self.center_object = center_obj
        self.center_name.setText('Name: ' + str(self.center_object.get_name()))
        self.center_location.setText('Location: ' + str(self.center_object.get_location().get_values()))
        self.center_velocity.setText('Velocity: ' + str(round(self.center_object.get_velocity().length(), 3)) + ' m/s')
        self.center_acceleration.setText('Acceleration: ' + str(round(self.center_object.get_acceleration().length(), 5)) + ' m/s^2')
        self.center_mass.setText('Mass: ' + str(self.center_object.get_mass()) + ' kg')
        self.center_density.setText('Density: ' + str(self.center_object.get_density()) + ' kg/m^3')
    
    
    def save_data(self):
        self.data_string += self.center_name.text() + '\n'
        self.data_string += self.center_location.text() + '\n'
        self.data_string += self.center_velocity.text() + '\n'
        self.data_string += self.center_acceleration.text() + '\n'
        self.data_string += self.center_mass.text() + '\n'
        self.data_string += self.center_density.text() + '\n' + '\n' + '\n'
        self.data_string += self.collision.text() + '\n'
        self.data_string += self.frame_rate.text() + '\n'
        self.data_string += self.time_step.text() + '\n'
        self.data_string += self.simulation_speed.text() + '\n'
        self.data_string += self.time_span.text() + '\n' + '\n'
        self.data_string += '----------------------------------\n'
        
        path = 'files/save.txt'
        FileReader.write_file(self, path)
        
        
        
    '''
    Functions for buttons
    '''
    
    '''
    Scales sizes of objects.
    '''
    def scale_size_m(self):
        self.scale_size = self.scale_size * (2 / 3)
        
        
    def scale_size_p(self):
        self.scale_size = self.scale_size * (3 / 2)
        
    
    '''
    Scales distances between objects.
    '''
    def scale_location_m(self):
        self.scale_location = self.scale_location * (2 / 3)
        
        
    def scale_location_p(self):
        self.scale_location = self.scale_location * (3 / 2)
        
    
    '''
    Scales distances between objects to the current size of them.
    '''
    def scale_dist_to_size(self):
        self.scale_location = self.scale_size
        
    
    '''
    Changes time step.
    '''
    def change_dt_m(self):
        if self.system.dt > 0.00125:
            self.system.dt = round(self.system.dt * 0.5, 5)
        
        
    def change_dt_p(self):
        if self.system.dt < 335544.32:
            self.system.dt = round(self.system.dt * 2, 5)
        
    
    '''
    Makes time step 0 and stores original value or sets stored value to time step when pause is pressed.
    '''
    def pause(self):
        if self.system.dt != 0:
            self.store_dt = self.system.dt
            self.system.dt = 0
        else:
            self.system.dt = self.store_dt
           
     
    '''
    Changes object that is centered to the screen (goes through list forward or backward).
    '''
    def center_object_p(self):
        index = self.system.get_objects().index(self.center_obj)
        if index == len(self.system.get_objects()) - 1:
            self.center_obj = self.system.get_objects()[0]
        else:
            self.center_obj = self.system.get_objects()[index + 1]
            
            
    def center_object_m(self):
        index = self.system.get_objects().index(self.center_obj)
        if index == 0:
            self.center_obj = self.system.get_objects()[len(self.system.get_objects()) - 1]
        else:
            self.center_obj = self.system.get_objects()[index - 1]
    
    
    '''
    Hides vectors
    '''
    def hide_vector(self):
        if self.hide_vectors == False:
            self.hide_vectors = True
        else:
            self.hide_vectors = False
    
    
    '''
    Creates new object to the system
    '''
    def new_object_to_scene(self):
        try:
            name = str(self.name_edit.text())
        
            location = str(self.location_edit.text()).split(',')
            for i in range(0,3):
                location[i] = float(location[i].strip())
            
            velocity = str(self.velocity_edit.text()).split(',')
            for i in range(0,3):
                velocity[i] = float(velocity[i].strip())
        
            mass = float(self.mass_edit.text())
        
            density = float(self.density_edit.text())
            
            self.value_error.hide()
            
            obj = Object(name, location, velocity, mass, density)
            self.system.new_object(obj)
            acc = VectorGraphics(obj, 'acceleration', self.perspective, self.center_obj, self.system)
            vel = VectorGraphics(obj, 'velocity', self.perspective, self.center_obj, self.system)
            obj_graphics = ObjectGraphics(obj, self.scale_size, self.scale_location, self.scale_size_diff, self.perspective, self.center_obj, self.system)
        
            self.scene.addItem(acc)
            self.scene.addItem(vel)
            self.scene.addItem(obj_graphics)
            self.added_objects.append(obj_graphics)
            self.added_vectors.append(acc)
            self.added_vectors.append(vel)
            
        except ValueError:
            self.value_error.setVisible(True)
        
    
    