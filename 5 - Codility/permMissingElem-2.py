# Created on Sat Sep 10 18:28:47 2016 || @author: axhufield

def permMissingElem(A):
    if A == []:
        return 1
        
    if len(A) == 1:
        return A[0] - 1
        
    B = []
    
    for e in A:
        B.append(e)
        if B[-1] > e:
            B.insert(0, e)
    print(B)
    
    inc = B[0]
    for r in B:
        if r != inc:
            return inc
        inc += 1
        
print(permMissingElem([2,3,5,1]))
