# Created on Mon Nov 14 20:13:50 2016 || @author: mxhfield

def permCheck(A):

    
    A.sort()
    inc = A[0]
    
    for e in A:
        if e != inc:
            return 0
        inc += 1
    return 1
    
    
print(permCheck([4, 1, 3, 2]))