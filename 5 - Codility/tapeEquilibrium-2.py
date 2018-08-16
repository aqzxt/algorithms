# Created on Fri Sep  9 22:50:29 2016 || @author: axhufield

def tapeEquilibrium(A):
    '''
    P = 1, difference = |3   − 10| = 7
    P = 2, difference = |4   −  9| = 5
    P = 3, difference = |6   −  7| = 1
    P = 4, difference = |10  −  3| = 7 
    '''
    diff = []
    if A == []:
        return min(diff)
    
    first = sum(A[:1])
    second = sum(A[1:])
    diff.append(abs(first - second))
    
    if len(A) > 1:    
        return tapeEquilibrium(A[1:])
    return A[0]
    
print(tapeEquilibrium([9, 7, 9, 3, 10, 4, 10]))
print(tapeEquilibrium([3,1,2,4,3]))
