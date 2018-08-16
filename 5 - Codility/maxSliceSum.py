# Created on Tue Nov  8 23:36:05 2016 || @author: mxhfield

def maxSliceSum(A):
    '''
    NOTE:
        Codility lesson not clear enough. In the example, it was shown as indexed and paired
        by side A[1, 2], A[4, 5] or as a standalone slice A[2, 2]
    
    Returns the maximum sum of any slice of A
    '''
    
    if len(A) == 0:
        return 0
    
    maxSum = A[0]
    
    left = 0
    right = 2
    
    while right <= len(A):
        
        temp = A[left]
        if temp > maxSum:
            maxSum = temp
        
        temp = sum(A[left:right])
        if temp > maxSum:
            maxSum = temp
            
        temp = A[right -1]
        if temp > maxSum:
            maxSum = temp
            
        temp = sum(A[left: len(A)])
        if temp > maxSum:
            maxSum = temp
        
        temp = sum(A[len(A) - left::-1])
        if temp > maxSum:
            maxSum = temp
            
        left += 1
        right += 1
        
    return maxSum
    

print(maxSliceSum([1, 1, 1]))
print(maxSliceSum([-2, 1]))
print(maxSliceSum([3, 2, -6, 4, 0]))
print(maxSliceSum([7, 0, 9, 12, 21, 49, 1]))