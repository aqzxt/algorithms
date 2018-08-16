# Created on Fri Sep  9 16:03:14 2016  ||  @author: axhufield


def evenList(A):
    '''
    A non-empty zero-indexed array A consisting of N integers is given.
    The array contains an odd number of elements, and each element of the array
    can be paired with another element that has the same value, except
    for one element that is left unpaired.
    '''
    same = []
    left = 0
    
    while left +1 < len(A):
        
        right = left +1
        while right < len(A):
            
            if A[left] == A[right]:
                same.append(A[right])
                
            right += 1
        left += 1
                
    for item in A:
        if not item in same:
            return item
    
    
print(evenList([2,4,7,5,9,1,7,9,3,1,5,3,2]))
