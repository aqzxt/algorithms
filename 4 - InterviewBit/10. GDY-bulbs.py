"""
Created on Sat Apr 14 13:41:15 2018 ----------- @author: mxhfield
"""

def bulbs(A):
    res = 0; flag = False
    for k in range(len(A)):
        
        if A[k] == 0 and not flag:
            res += 1
            flag = True
            
        if A[k] == 1 and flag:
            res += 1
            flag = False
#        print(res, flag, A[k:])
    return res
            
a = [1, 1, 0, 0, 1, 1, 0, 0, 1]
b = [1, 1, 1]

print(bulbs(b))