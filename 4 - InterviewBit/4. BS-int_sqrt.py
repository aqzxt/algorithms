"""
Created on Thu Mar 15 07:26:48 2018 ----------- @author: mxhfield
"""

def int_sqrt(A):
    if A <= 0:
        return 0
    if A == 1:
        return 1
    
    div = A//2
    if A > 30:
        while div * div >= A:
            div //= 2
            
    lo = 1
    hi = div*2
    mid = (hi-lo)//2
    while lo < hi:
        print(lo, mid, hi)
        
        if mid*mid == A or mid*mid < A < (mid+1)*(mid+1):
            return mid
        
        if (mid-1)*(mid-1) < A < (mid)*(mid):
            return mid-1
        
        if mid*mid > A:
            hi = mid+1
            mid = mid//2
        else:
            lo = mid
            mid += (hi-lo)//2
    
    return int(div)
    
#print(int_sqrt(11))
#print(int_sqrt(2030))
print(int_sqrt(14))