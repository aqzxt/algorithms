"""
Created on Wed Feb 28 21:23:07 2018 ----------- @author: mxhfield
"""

def wave_array(A):
    A.sort()
    for e in range(0,len(A),2):
        if e +1 != len(A):
            if A[e] == A[e+1]:
                continue
            A[e], A[e+1] = A[e+1], A[e]
    return A

a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(wave_array(a2))