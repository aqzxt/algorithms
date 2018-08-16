# Created on Sat Nov 19 02:33:58 2016 || @author: mxhfield

def tapeEquilibrium(A):
    
    if len(A) == 1:
        return A[0]

    inc = 1
    flag = True
    
    while inc < len(A):
        
        temp = abs( sum(A[:inc]) - sum(A[inc:]) )
        
        if flag:
            last = temp
            flag = False
            
        if temp < last:
            last = temp
            
        inc += 1
            
    return last
    
    
    
    
    
print(tapeEquilibrium([3, 1]))    
print(tapeEquilibrium([3, 1, 2, 4, 3]))