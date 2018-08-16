"""
Created on Sun Mar  4 00:43:52 2018 ----------- @author: mxhfield
"""

def maximumGap(A):
    '''First step:
        make a list to record the min number (at its position/index)
        to the left - The leftmost minimum number. O(N) space
    
        Second step:
            make another list to record the max number (at its position/index)
            to the right - The rightmost maximum number. +O(N) space
        
        Third/Final step:
            iterate the list to count how many jumps (a gap) are between
            min and max number recorded number in previous steps. O(N) runtime
            
        # @param A : tuple of integers
        # @return an integer
    '''
    n = len(A)
    if n == 1:
        return 0
    
    left = [0]*n; left[0] = A[0]
    for k in range(1, n):
        left[k] = min(left[k-1], A[k])
    print(left)
    
    right = [0]*n; right[-1] = A[-1]
    for k in range(n-2, -1, -1):
        right[k] = max(right[k+1], A[k])
    print(right)
    print()
    
    k = 0; e = 0; answer = -1
    while k < n and e < n:
        print('left[k] _',left[k],'<=', right[e], '_ right[e]',answer)
        if right[e] >= left[k]:
            answer = max(answer, e-k)
            e += 1
        else:
            k += 1
    return answer

a1 = (4, 9, 19, 10, 5, 0, 3, 6, 12, 1)

print(maximumGap(a1))