"""
Created on Tue Feb 27 17:17:30 2018 ----------- @author: mxhfield
"""

def rotate_array(a, b):
    if len(a) == 1:
        return a
    
    answer = []
    # limit b when bigger than len(a)
    if abs(b) > len(a):
        b = b % len(a)
    
    for i in range(len(a)):
        answer.append(a[b])
        b += 1
        
        if abs(b) == len(a):
            b = 0
    return answer


a = [14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35]
b = 51 # [96, 62, 32, 98, 77, 35, 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33]
b2 = 56 # [35, 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77]

a2 = [1]
b3 = 1

print(rotate_array(a, 51))

