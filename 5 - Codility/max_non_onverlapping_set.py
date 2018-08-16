"""
Created on Thu May 17 02:22:47 2018 ----------- @author: mxhfield

    A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6        {0, 2, 3}, {0, 2, 4}, {1, 2, 3} or {1, 2, 4}
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9        Returns 3 non-overlapping set
    A[4] = 9    B[4] = 10       containing the maximal number of segments
"""

A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]

def max_set(A, B):
#    pairs = [(A[e], B[e]) for e in range(len(A))]
#    print(pairs)
    pairs = []
    for i in range(len(A)-1):
        
        if B[i] < A[i+1]:
            pairs.append((A[0], B[0]))
            
        
    
    
    
    
print(max_set(A, B))