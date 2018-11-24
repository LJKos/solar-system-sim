'''
Created on 30 Mar 2018

@author: lauri
'''
from system import System
from object import Object


'''
FileReader defines methods for reading and writing files.
It reads a file and creates objects to System and writes data string to a file.
'''
class FileReader():
    
    def __init__(self, system):
        self.system = system
        
        self.name = ""
        self.location = ""
        self.velocity = ""
        self.mass = ""
        self.density = ""
       
     
    '''
    Function for reading objects from a file.
    '''
    def read_file(self):
        try:
            file = open("files/start_file.txt", "r")
            
            self.line_reader(file)
                    
            file.close()
        except OSError:
            print("Could not read the file!")
            
    
    '''
    Function for read_file that reads lines in the text file.
    '''
    def line_reader(self, file):
        name = False
        location = False
        velocity = False
        mass = False
        density = False
        
        for line in file:
            line = line.strip()
            
            if line != "":
                if line[0] == '#':
                    if name == True and location == True and velocity == True and mass == True and density == True:
                        self.system.new_object(Object(self.name, self.location, self.velocity, self.mass, self.density))
                
                    name = False
                    location = False
                    velocity = False
                    mass = False
                    density = False
                    
                    self.name = line[1:int(len(line))]
                    name = True
                
                elif line[0:1] != "//" or line.strip() == "":
                    word = line.split(':')
                
                    if word[0].strip() == "location":
                        data = word[1].split(',')
                        self.location = [float(data[0].rstrip()), float(data[1].rstrip()), float(data[2].rstrip())]
                        location = True
                    
                    elif word[0].strip() == "velocity":
                        data = word[1].split(',')
                        self.velocity = [float(data[0].rstrip()), float(data[1].rstrip()), float(data[2].rstrip())]
                        velocity = True
                    
                    elif word[0].strip() == "mass":
                        self.mass = float(word[1].rstrip())
                        mass = True
                    
                    elif word[0].strip() == "density":
                        self.density = float(word[1].rstrip())
                        density = True
            
        if name == True and location == True and velocity == True and mass == True and density == True:
            self.system.new_object(Object(self.name, self.location, self.velocity, self.mass, self.density))
            
    
    '''
    Function for writing object information to a file.
    '''
    def write_file(self, file_path):
        file = open(file_path, 'w')
        file.write(self.data_string)
        file.close()
    
    
