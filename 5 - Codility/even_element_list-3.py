# Created on Fri Sep  9 18:09:37 2016  ||  @author: axhufield


def lonelyInt(A):
    '''
    A non-empty zero-indexed array A consisting of N integers is given.
    The array contains an odd number of elements, and each element of the array
    can be paired with another element that has the same value, except
    for one element that is left unpaired.
    '''
    if A == []:
        return []
    
    previous = []
    previous.append(A[0])
    if not A[0] in A[1:] and not A[0] in previous[:-1]:
        return A[0]
        
    return lonelyInt(A[1:])
    
print(lonelyInt([9, 3, 9, 3, 9, 7, 9]))
