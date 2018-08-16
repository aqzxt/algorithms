# Created on Fri Sep  9 16:41:51 2016  ||  @author: axhufield


def lonelyInt(A):
    '''
    A non-empty zero-indexed array A consisting of N integers is given.
    The array contains an odd number of elements, and each element of the array
    can be paired with another element that has the same value, except
    for one element that is left unpaired.
    '''
    inc = 1
    previous = []
    
    if type(A) != list:
        return A
    
    for e in A:
        if not e in A[inc:] and not e in previous:
            return e
        previous.append(e)
        inc += 1
        
print(lonelyInt(42))
            
