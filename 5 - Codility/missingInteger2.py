# Created on Thu Nov 10 23:46:00 2016 || @author: mxhfield

def missingInteger(A):
    '''
    100% Score on Codility (Correctness and Performance)
    
    Given a non-empty zero-indexed array A of N integers,
    returns the minimal positive integer (greater than 0) that does not occur in A
    '''
    A.sort()
    inc = 0
    miss = [A[0]]
    
    # get rid of the NEGATIVES, or if first element is BIGGER than 1
    if A[-1] <= 0 or A[0] > 1:
        return 1
        
    # if first element is NEGATIVE
    if A[0] < 0:
        try:
            A = A[A.index(0):]
        except:
            A = A[1:]
        else:
            inc = A[0]

    flag = True
    for e in A:

        if e > 0 and e > miss[-1]:
            
            if flag:
                
                inc = e -1
                flag = False

            inc += 1

            if e > inc:
                return inc

            miss.append(e)
        
    if A[0] > 1:
        return 1
    return A[-1] +1
    
print(missingInteger([1, 3, 6, 4, 1, 2]))
print(missingInteger([-1, 1, 2, 3]))
print(missingInteger([-2147483648, 2147483647]))

print(missingInteger([-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, 
                    -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, 
                    -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, 
                    -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, 
                    -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
