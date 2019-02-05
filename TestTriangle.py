# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,1,2 should be Isoceles')
    
    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(2,1,2),'Isoceles','2,1,2 should be Isoceles')
    
    def testIsocelesTrianglesC(self): 
        self.assertEqual(classifyTriangle(2,2,1),'Isoceles','2,1,1 should be Isoceles')
    
    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(7,9,15),'Scalene','7,9,15 should be Scalene')

    def testNotATrianglesA(self): 
        self.assertEqual(classifyTriangle(10,20,2),'NotATriangle','10,20,2 should be NotATriangle')
    
    def testNotATrianglesB(self): 
        self.assertEqual(classifyTriangle(10,2,20),'NotATriangle','10,2,20 should be NotATriangle')
    
    def testNotATrianglesC(self): 
        self.assertEqual(classifyTriangle(2,10,20),'NotATriangle','2,10,20 should be NotATriangle')

    def testValidInputA(self): 
        self.assertEqual(classifyTriangle(0,0,0),'NotATriangle','0,0,0 should be NotATriangle')
    
    def testValidInputB(self): 
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','200,200,200 should be Equilateral')
    
    def testInValidInputA(self): 
        self.assertEqual(classifyTriangle(-4,-3,-5),'InvalidInput','-4,-3,-5 are InvalidInput')
    
    def testInValidInputB(self): 
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','201,201,201 are InvalidInput')
    
    def testInValidInputC(self): 
        self.assertEqual(classifyTriangle("3","4","5"),'InvalidInput','"3","4","5" are InvalidInput')
    
    def testInValidInputD(self): 
        self.assertEqual(classifyTriangle('5','5','5'),'InvalidInput',' char are InvalidInput')
    
    def testInValidInputE(self): 
        self.assertEqual(classifyTriangle(2.5,5.7,2.5),'InvalidInput','2.5,5.7,2.5 are InvalidInput')
    
    def testInValidInputF(self): 
        self.assertEqual(classifyTriangle(2.5,7,4),'InvalidInput','2.5,7,4 are InvalidInput')
    
    def testInValidInputG(self): 
        self.assertEqual(classifyTriangle(2,7,"4"),'InvalidInput','2.5,7,"4" are InvalidInput')
    
    def testInValidInputH(self): 
        self.assertEqual(classifyTriangle(2,'7',4),'InvalidInput','char are InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

