# Created on Fri Sep 16 15:48:09 2016 || @author: axhufield

def missingInteger(A):
    '''
    Given a non-empty zero-indexed array A of N integers
    Returns the minimal positive integer (greater than 0) that does not occur in A
    '''
    A.sort()
    inc = 1
    
    if A[-1] <= 0:
        return 1
        
    # single element list
    if len(A) == 1:
        if A[0] == 1:
            return 2
        return A[0] -1
        
    while inc < len(A):
        # subtract current with previous
        if abs(A[inc] - A[inc -1]) == 2:
            # return positive integers only
            if A[inc] < 0:
                return 1
            return inc
        inc += 1