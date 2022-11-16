#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Week two Exercise 2
Put your function from last week’s exercise (5) in a script, 
with documentation. Import into the interpreter, 
access help and test function works as expected. 
Add an example as a docstring.

Example:
    X = np.array(array([8, 7, 7, 9, 2, 4, 4, 1, 1, 5]))
    n = 6
    f(X,n) = [2, 1, 1]

Created on Wed Nov 16 09:58:59 2022

@author: Ross Erskine
"""

def f(X, n):
    divisible = []
    for x in X:
        if n % x == 0:
            divisible.append(x)
        
    return divisible

if __name__ == '__main__': 
    
########################## Testing ##########################################
    import unittest
    import numpy as np
    
    class TestF(unittest.TestCase):
        """ Test f function """
        
        def test_Pararmeters_default(self):
            """ test Parameter class defaults"""
            
            X = np.array([5, 6, 8, 4, 2, 1, 3, 1, 8, 1])
            n= 5
            self.assertEqual(f(X,n), [5, 1, 1, 1])
        
        
    unittest.main()