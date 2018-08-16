"""
Created on Tue May 15 14:12:07 2018 ----------- @author: mxhfield
"""
from math import sqrt
from math import ceil

def is_power(A):
    x = ceil(sqrt(A))
    if A == 1 or x * x == A: return 1
    for i in range(2, x+1):
        res = i
        for k in range(i, x+1):
            res *= i
            if res == A: return 1
    return 0

print(is_power(144))