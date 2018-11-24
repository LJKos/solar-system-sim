'''
Created on 7 Mar 2018

@author: lauri
'''
from system import System
from object import Object
from physics import Physics
from vector import Vector
from gui import GUI
import unittest

'''
Test class is for testing the program.
Normally not used.
'''
class Test(unittest.TestCase):
    
    def setUp(self):
        self.system = System(0.02)
        
        maa = Object("Maa", [1.4960*(10**8)*(10**3),0,0], [0,29800,0], 5.974*10**24, 5517)
        kuu = Object("Kuu", [385400000+1.4960*(10**8)*(10**3),0,0], [0,1023+29800,0], 5*10**22, 3344)
        
        self.system.new_object(maa)
        self.system.new_object(kuu)
        
    
    def test_objects(self):
        self.assertEqual(len(self.system.get_objects()), 2, "There should be two objects in the system.")
        
        
    def test_new_object_location(self):
        self.system.update_objects()
        
        self.assertEqual(self.system.get_objects()[0].get_location().get_values(), [149600000000.0, 596.0, 0.0], "Wrong location (Maa).")
        self.assertEqual(self.system.get_objects()[1].get_location().get_values(), [149985400000.0, 616.4600000000017, 0.0], "Wrong location (Kuu).")
        
    
    def test_collision(self):
        crasher1 = Object("c1", [0,0,0], [0,0,0], 100, 100)
        crasher2 = Object("c2", [1,0,0], [0,0,0], 100, 100)
        
        self.system.new_object(crasher1)
        self.system.new_object(crasher2)
        
        self.system.update_objects()
        
        self.assertTrue(self.system.get_collision(), "Collision should be True")
        
        
    
if __name__ == "__main__":
    unittest.main()