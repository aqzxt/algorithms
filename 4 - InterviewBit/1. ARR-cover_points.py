"""
Created on Wed Feb 28 03:06:23 2018 ----------- @author: mxhfield
"""

def cover_points(A, B):
    steps = 0
    for k in range(len(A)-1):
        
        first = abs(A[k] - A[k+1])
        second = abs(B[k] - B[k+1])
        
        steps += max(first, second)
        
    return steps

A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]

print(cover_points(A, B))