"""
Created on Fri Mar  2 22:15:48 2018 ----------- @author: mxhfield
"""
from math import sqrt

def allFactors(A):
    L = []
    for k in range(1, int(sqrt(A)) +1):
        
        if A % k == 0:
            L.append(k)
            
            print(sqrt(A), k, A/k)
            if k < sqrt(A):
                L.append(int(A/k))
    print(L)
    L.sort()
    return(L)

#print(allFactors(85463))
print(allFactors(144))