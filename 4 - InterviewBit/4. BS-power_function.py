"""
Created on Fri Mar 16 00:57:48 2018 ----------- @author: mxhfield
"""

def power_function(x, n, d):
    '''
            x ^ n = (x * x) ^ n/2
    '''
    if not x or not d: # division by zero
        return 0
    if not n or x < 0 and n > 1: # case when x**n is negative
        return 1
    
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    res = x
    
    if x > 1:
        inc = 0
        while inc < n:
            
            # prevent overflow
            if (res*x) >= MAX_INT:
                return res % d
            if (res*x) <= MIN_INT:
                return res % d
            
            res *= x
            inc += 1
    print(res, d, res%d)
    return res %d

#print(power_function(71045970, 41535484, 64735492))
#print(power_function(-1, 2, 20))
#print(power_function(-1, 1, 20))
print(power_function(2, 3, 3))