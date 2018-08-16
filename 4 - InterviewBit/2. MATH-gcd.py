"""
Created on Sat May 12 20:44:32 2018 ----------- @author: mxhfield
"""

def gcd(A, B):
    if not A and not B: return 0
    
    if A == B: return A
    ma = max(A, B); mi = min(A, B); x = mi
    if not mi: return ma
    while 1:
        print(mi % x, ma % x, x)
        if (mi % x == 0 and ma % x == 0) or (x == 1): return x
        x -= 1

print(gcd(4, 28))