# Created on Fri Sep  9 18:36:17 2016 || @author: axhufield

def rotation(A, K):
    '''
    A zero-indexed array A consisting of N integers is given. 
    Rotation of the array means that each element is shifted right by one index, 
    and the last element of the array is also moved to the first place.
    '''
    if A == []:
        return A
    for e in range(K):
        last = A[-1]
        del A[-1]
        A.insert(0, last)
    return A


print(rotation([3, 8, 9, 7, 6], 3))                
print(rotation([], 1))
