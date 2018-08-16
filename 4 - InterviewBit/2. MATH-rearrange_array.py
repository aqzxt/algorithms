"""
Created on Sun May 13 01:24:00 2018 ----------- @author: mxhfield
"""

'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

 A : [ 4, 0, 2, 1, 3 ]
 
  3 4 2 0 1 
'''

def rearrange_array(A):
    n = len(A)
    for i in range(n):
        A[i] += (A [A[i] ] % n) *n
    for i in range(n):
        A[i] = A[i] //n
        
def rearrange_array2(A):
    n = len(A)
    B = [0]*n
    for i in range(n):
        B[i] = A[A[i]]
    for i in range(n):
        A[i] = B[i]