# Created on Sun Sep 11 00:01:48 2016  ||  @author: axhufield


def distinct(A):
    '''
    Given list A as "[2,1,1,2,3,1]" the function should return 3
    Because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
    '''
    if A == []:
        return 0
    A.sort()
    B = []
    B.append(A[0])
    for e in A:
        if B[-1] != e:
            B.append(e)
    return len(B)
