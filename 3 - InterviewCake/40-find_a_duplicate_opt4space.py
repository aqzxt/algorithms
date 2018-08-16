"""
Created on Tue Mar 27 19:50:53 2018 ----------- @author: mxhfield
"""

def find_a_duplicate(A):
    
    for k in range(len(A)):
        
        lo = 0, hi = len(A)-1
        while lo < hi:
            mid = (hi - lo) //2
            
            if A[mid] == A[mid+1] or A[mid-1] == A[mid]:
                return A[mid]
            
            



a = [2, 4, 9, 1, 63, 90, 71, 42, 55, 6, 9, 1, 64, 37, 32, 71, 67]
b = [0]*len(a)

