"""
Created on Mon Mar 19 07:13:26 2018 ----------- @author: mxhfield
"""

def merge_2sorted_arrays(A, B):
    '''Merge two sorted arrays IN-PLACE
            A.sort()
    
    '''
    if not A or not B:
        return A + B
    
    if A[-1] <= A[0]:
        return A + B
    
    k = e = 0
    while e < len(B):
        
        if A[k] > B[e]:
            A[k], B[e] = B[e], A[k]
        k += 1
            
        if k == len(A):
            e += 1
            k = 0
    
    if len(B) > 1:
        k, e = 0, 1
        while k < len(B):
            
            if B[k] > B[e]:
                B[k], B[e] = B[e], B[k]
            e += 1
            
            if e == len(B):
                k += 1
                e = k
    
    A += B
    a = ''
    for k in A:
        a += str(k) + ' '
    print(a,)
    return ''


#print(merge_2sorted_arrays([-5], [-5]))
#print(merge_2sorted_arrays([1, 5, 8], [6, 9]))
#print(merge_2sorted_arrays([-2, 3], [-4, -1]))
#print(merge_2sorted_arrays([-4, 3], [-2, -2]))
print(merge_2sorted_arrays([1, 2, 5, 6, 9, 13, 54], [-1, 2]))
#print(merge_2sorted_arrays([0, 1, 2], [-3,-1, 2]))