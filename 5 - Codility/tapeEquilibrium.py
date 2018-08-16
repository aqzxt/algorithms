# Created on Fri Sep  9 22:13:04 2016 || @author: axhufield

def tapeEquilibrium(A):
    '''
    P = 1, difference = |3   − 10| = 7
    P = 2, difference = |4   −  9| = 5
    P = 3, difference = |6   −  7| = 1
    P = 4, difference = |10  −  3| = 7 
    '''
    inc = 1
    diff = []
    
    if A == []:
        return 0
    
    if len(A) == 1:
        return A[0]
        
    if len(A) == 2:
        return abs(A[0] - A[1])
    
    while inc +1 < len(A):
        first = sum(A[:inc])
        second = sum(A[inc:])
        diff.append(abs(first - second))
        inc += 1
        
    return min(diff)
    

print(tapeEquilibrium([9, 7, 9, 3, 10, 4, 10]))
print(tapeEquilibrium([3,1,2,4,3]))
