"""
Created on Sat Mar 31 00:53:49 2018 ----------- @author: mxhfield
"""

def reverse_bits(A):
    A = '{0:032b}'.format(A)
    return int(''.join( [A[k] for k in range(len(A)-1, -1, -1)] ), 2)
    
#print(reverse_bits(3))

def reverse_bits2(A):
    return int(bin(A)[2:][::-1].ljust(32, "0"), 2)


def reverse_bits3(A):
    result = 0
    for i in range(32):
        if (A >> i) & 1: result |= 1 << (32 - 1 - i)
    return result

