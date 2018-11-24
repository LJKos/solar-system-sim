'''
Created on 23 Mar 2018

@author: lauri
'''

import sys
from system import System
from object import Object
from physics import Physics
from vector import Vector
from gui import GUI
from file_reader import FileReader
from PyQt5.QtWidgets import QApplication

'''
Starts the simulation for normal usage.
'''
def main():
    
    system = System(0.02)
    reader = FileReader(system)
    reader.read_file()
    
    global app
    app = QApplication(sys.argv)
    gui = GUI(system)
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()