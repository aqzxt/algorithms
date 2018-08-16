"""
Created on Sun Mar 18 02:18:16 2018 ----------- @author: mxhfield
"""

def diff_possible(A, B):
    if len(A) < 2:
        return 0
    e = 0
    k = 1
    while e < len(A)-1:
        print(e, k, '===',A[e], A[k])
        
        if abs(A[k] - A[e]) == B:
            return 1
        elif k +1 == len(A):
            e += 1
            k = e+1
        else:
            k += 1
    return 0
    
    
print(diff_possible([1, 3, 5], 4))
print(diff_possible([1, 2, 2, 3, 4 ], 0))
#print(diff_possible([1, 2, 3], 0))
#print(diff_possible([0, 1], 0))