"""
Created on Tue Mar 20 17:33:56 2018 ----------- @author: mxhfield
"""

def remove_duplicates(A):
    if len(A) < 3:
        return len(A)
    
    count = e = 0
    k = 1
    unequal = None
    while k < len(A):
        
        print(A, count,'==e',A[e],A[k],'k==', e, k,'==',count, unequal)
        
        if A[k-1] == A[k]:
            if unequal:
                A[e], A[k] = A[k], A[e]
                e += 1
            else:
                count = 1
        
        
        # if unequal and count, then it's more than twice
        elif A[k-1] != A[k] and count:
            unequal = A[k-1]
            e = k-1
            A[e], A[k] = A[k], A[e]
            count = 0
            
#        else:
#            A[e], A[k-1] = A[k-1], A[e]
#            e += 1
#            A[e], A[k] = A[k], A[e]
#            e += 1
            
            print(A[k-1], A[k], e)
        
        k += 2
        
    return A
    
a = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 7]
print(remove_duplicates(a))