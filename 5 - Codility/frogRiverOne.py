# Created on Fri Sep 16 18:01:24 2016 || @author: axhufield


def frogRiverOne(X, A):
    if len(A) == 1 or len(A) < X +1:
        return -1
    return A[0] + A[X +1]
