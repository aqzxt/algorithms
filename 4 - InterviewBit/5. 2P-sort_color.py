"""
Created on Mon Mar 19 05:05:39 2018 ----------- @author: mxhfield
"""

def sort_color(A):
    if not A:
        return 0
    
    colors = [0] * 3
    for k in A:
        if not k:
            colors[0] += 1
        if k == 1:
            colors[1] += 1
        else:
            colors[2] += 1
    
    e = k = 0
    current = colors[e]
    
    while True:
        
        if k == 0:
            A[e] = 0
        if k == 1:
            A[e] = 1
        if k == 2:
            A[e] = 2
            
        if e +1 == current:
            k += 1  
            current += colors[k]
            
        e += 1
        if e == len(A):
            break
    return A
    
print(sort_color([0, 1, 2, 0, 1, 2]))
print(sort_color([1, 0, 0]))