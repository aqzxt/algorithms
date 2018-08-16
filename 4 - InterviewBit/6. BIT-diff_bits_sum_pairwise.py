"""
Created on Sat Mar 31 05:39:50 2018 ----------- @author: mxhfield
"""
import time

def diff_bits_sum_pairwise(A):
    start = time.clock()
    for k in range(len(A)):
        A[k] = '{0:b}'.format(A[k])
    
    count = i = 0; k = 1
    while i+1 < len(A) and k +1 <= len(A):
        
        first, second = A[i], A[k]
        len1, len2 = len(first), len(second)
        
        if len1 > len2:
            second = ''.ljust(len1 - len2, '0') + second
        if len2 > len1:
            first = ''.ljust(len2 - len1, '0') + first
        
        e = max(len1, len2)-1
        while e >= 0:
            
            if first[e] == '0' and second[e] == '1' \
                or first[e] == '1' and second[e] == '0':
                    count += 2
            e -= 1
        k += 1
        
        if k == len(A):
            i += 1
            k = i+1
            
    end = time.clock()
    return count, end-start
    

print(diff_bits_sum_pairwise([1, 3, 5]))