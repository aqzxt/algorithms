"""
Created on Sun Apr  1 06:29:37 2018 ----------- @author: mxhfield
"""

def three_sum_closest2(A, B):
    if len(A) == 3: return sum(A)
    if len(A) <= 2: return 0
    
    current = [0]*3
    so_far = A[:3]
    the_sum = sum(so_far) - B
    for k in range(3,len(A)):
        
        print(so_far, '=======', current)
        
        s0, s1, s2 = so_far[0], so_far[1], so_far[2]
        
        current[0] = s1 + s2 + A[k]
        if current[0] < 0:
            current[0] = current[0] + B
        else:
            current[0] = current[0] - B
            
        current[1] = s0 + s2 + A[k] - B
        if current[1] < 0:
            current[1] = current[1] + B
        else:
            current[1] = current[1] - B
            
        current[2] = s0 + s1 + A[k] - B
        if current[2] < 0:
            current[2] = current[2] + B
        else:
            current[2] = current[2] - B
        
        smaller = (current[0], 0)
        for e in range(1,3):
            if current[e] > 0 and current[e] < smaller[0]:
                smaller = (current[e], e)
        
        so_far[e] = A[k]
        the_sum = sum(so_far)
            
    return the_sum
            
            

















def three_sum_closest(A, B):
    if len(A) == 3: return sum(A)
    if len(A) <= 2: return 0
    
    A = set(A); A = list(A); A.sort()
    target = i = 0
    lo, hi = 0, len(A)-1; mid = (hi-lo)//2
    while lo < hi:
        mid = (hi-lo)//2
        
        
        print(lo, mid, hi, A[mid])
        print(A)
        print()
        
        if A[mid] == B or A[mid-1] < B < A[mid]:
            target = mid
            break
            
        if B > A[mid]:
            hi = mid
        else:
            lo = mid
        
        i+=1
        if i==10:
            break
    return target















a = [6, -6, 2, 6, -7, -3, 4, -5, 3, -10, -5, 8, -5, 1, -4, -8, -6, 4, -1, 10, -10, 0, 6, -4, -7, -6, 4, 0, 1, -5, 7, 5, 0, 0, 2, -3, 10, -8, -3, 7, -5, 7, 4, 5, 3, 6, 7, -4, 8, 0, -5, -5, 2, 4, -8, 1, -5, -1]
b = [-5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3]
#print(three_sum_closest([-1, 2, 1, -4], 2))
#print(three_sum_closest(a, -4)) # -4
print(three_sum_closest(b, -1)) # -1