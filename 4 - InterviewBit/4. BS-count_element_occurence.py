"""
Created on Thu Mar 15 03:32:43 2018 ----------- @author: mxhfield
"""

def count_element_occurence(A, target):
    if len(A) <= 1:
        if A[0] == target: return 1
        else: return 0
    
    # when target is NOT in A
    if target < A[0] or target > A[-1]: return 0
    
    i, res = 0, []
    if A[0] == target:
        res.append(0)
        i += 1
    
    while i < 2:
        lo, hi, mid = 0, len(A)-1, len(A)//2
        while lo < hi:
            print(i, mid, '===',A[mid-1], A[mid], A[mid+1],'===',lo,hi, res)
            
            # last item is the target
            if i and A[-1] == target:
                res.append(len(A)-1)
                break
            
            if i or A[mid] <= target:
                if A[mid] == target and A[mid+1] != target:
                    res.append(mid)
                    break
                
                if A[mid] <= target: # offender !!!
                    lo = mid
                    mid += (hi-lo)//2
                    
                else:
                    hi = mid
                    mid = mid//2
            
            if not i and A[mid] >= target:
                if A[mid-1] != target and A[mid] == target:
                    res.append(mid)
                    break
                
                if A[mid] >= target:
                    hi = mid
                    mid = mid//2
                    
                else:
                    lo = mid
                    mid += (hi-lo)//2
            
            # case where target COULD be in the middle, BUT it's NOT.
            elif A[mid-1] < target < A[mid] or A[mid] < target < A[mid+1]:
                break
            
        i += 1
        
    if not res:
        return 0
    return abs(res[0] - res[1]) +1


print(count_element_occurence([5, 7, 7], 8))
print(count_element_occurence([5, 7, 7, 8, 8, 8, 8, 10], 8))