"""
Created on Thu Mar  8 00:14:48 2018 ----------- @author: mxhfield
"""

	# @param A : list of integers
	# @return a list of integers
def plusOne(A):
    if A:
        if A[-1] != 9:
            A[-1] += 1

        else:
            for k in range(len(A)-1, -1, -1):
                if A[k] != 9:
                    A[k] += 1
                    break
                elif k == 0 and A[k] == 9:
                    A[k] = 0
                    A.insert(0, 1)
                else:
                    A[k] = 0
        if A[0] != 0:
            return A   
        
        for i in range(len(A)):
            if A[i]:
                return A[i:]
    return A


print(plusOne([0, 0, 3, 7, 6, 4, 0, 5, 5, 5]))
print(plusOne([9, 9, 9, 9, 9, 9, 9]))