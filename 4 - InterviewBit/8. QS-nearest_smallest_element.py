"""
Created on Sun May 20 20:08:30 2018 ----------- @author: mxhfield
"""

def prev_smaller(A):
    answer = []
    stack = []
    for i in range(len(A)):
        
        while stack:
            if stack[-1] >= A[i]:
                stack.pop()
            else:
                break
        if stack:
            answer.append( stack[-1] )
        else:
            answer.append(-1)
        
        stack.append(A[i])
        
    return answer

a = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ] #  [-1, 34, -1, 27, -1, 5, 28, 5, 20]

print(prev_smaller(a))

