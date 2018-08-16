"""
Created on Sat Mar 31 03:11:22 2018 ----------- @author: mxhfield
"""

def single_duplicate(A):
    ''' Cancel out each pair by XORing them '''
    x = 0
    for k in A:
        x ^= k
    return x



def single_duplicate2(A):
    ans = 0
    for x in A:
        ans = ans^x
    return ans



def single_duplicate3(A):
    ret = A[0]
    for i in range(1,len(A)):
        ret ^= A[i]
    return ret