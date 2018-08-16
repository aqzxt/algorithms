# Created on Sat Sep 10 19:36:56 2016 || @author: axhufield

def permCheck(A):
    A.sort()
    inc = A[0]
    for e in A:
        if inc != e:
            return 0
        inc += 1
    return 1
    
#print(permCheck([4,1,3,2]))


def permCheck2(A):
    '''
    A permutation is a sequence containing each element from 1 to N once, and only once.
    Returns 1 if array A is a permutation "[4,1,3,2]" and 0 if it is not "[4,1,3]".
    '''
    if  A == []:
        return 0
    if len(A) == 1:
        return 1
    A.sort()
    inc = 1
    while inc < len(A):
        if A[inc] - A[inc -1] != 1:
            return 0
        inc += 1
    return 1
    
print(permCheck2([4,1,3,2,8,0,5,7,9]))
