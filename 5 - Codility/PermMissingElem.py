# Created on Sat Sep 10 17:56:43 2016 || @author: axhufield

def permMissingElem(A):
    '''
    N is an integer within the range [0..100,000]
    the elements of A are all distinct
    each element of array A is an integer within the range [1..(N + 1)]
    '''
    A.sort()
    
    if A == []:
        return 1
        
    if len(A) == 1 and A[0] != 1:
        return A[0] -1
        
    inc = A[0]
    for e in A:
        if inc != e:
            return inc +1
        inc += 1
        
    if A[0] == 1:
        return inc
    return A[0] -1
        
print(permMissingElem([4]))
print(permMissingElem([2,3,5,1]))
