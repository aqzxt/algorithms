# Created on Fri Sep  9 19:42:32 2016 || @author: axhufield

def rotation(A, K):
    '''
    A zero-indexed array A consisting of N integers is given. 
    Rotation of the array means that each element is shifted right by one index, 
    and the last element of the array is also moved to the first place.
    '''
    A.reverse()
    inc = K * len(A)
    
    while inc +1 > 0:
        left = 0
        right = 1 
        
        while right < len(A):
            
            temp = A[right]
            A[right] = A[left]
            A[left] = temp
            
            left += 1
            right += 1
            
            if right +1 == len(A):
                temp = A[0]
                A[0] = A[right]
                A[right] = temp
        
        inc -= 1
        
    A.reverse()
    return A
                
print(rotation([3, 8, 9, 7, 6], 3))
