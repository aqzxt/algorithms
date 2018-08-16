# Created on Wed Nov  9 20:26:12 2016 || @author: mxhfield

def passingCars(A):
    '''
    Given a non-empty zero-indexed array A of N integers
    Returns the number of pairs of passing cars
    '''
    passing = 0
    inc = 1
    
    while inc < len(A):
        
        print("first ",A[0],"---- second ",A[inc], "---",inc)
        if A[0] == False and A[0] != A[inc]:
            passing += 1
            print(passing,"\n")
            
        inc += 1
        if inc == len(A):
            del A[0]
            inc = 0
            
        if passing > 1000000000:
            return -1
            
    return passing
    
print(passingCars([1, 0]))
print("\nTest case break line\n")
print(passingCars([1, 0, 1, 1, 1]))






    
#    left = 0
#    right = 1    
#    while left < len(A):
#        
#        if A[left] != A[right]:
#            passing += 1
#        
#        
#        if right + 1 == len(A):
#            left += 1
#            right = left +1
#            
#        right += 1
#        
#    return passing