"""
Created on Tue May 15 22:43:46 2018 ----------- @author: mxhfield
"""

def squareSum(A):
    s = {}
    a = 0
    while a*a < A:
        b = 0
        while b*b < A:
            if (a * a) + (b * b) == A and s.get(a) == None and s.get(b) == None:
                s[a] = [a, b]
            b += 1
        a += 1
    return list(s.values())
    
print(squareSum(5))