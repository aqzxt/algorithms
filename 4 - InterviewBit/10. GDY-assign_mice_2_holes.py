"""
Created on Thu Apr 12 12:57:12 2018 ----------- @author: mxhfield
"""

def assign_mice_2_holes(A, B):
    if len(A) == 1:
        return abs(A[0] - B[0])
    
    a, b = abs(A[0] - B[0]), abs(A[0] - B[1])
    for k in range(1, len(A)):
        a = max(a, abs(A[k] - B[k]))
        b = max(b, abs(A[k] - B[k-1]))
        print(a, b, abs(a-b))
    return abs(a - b)

a = [4, -4, 2]; b = [4, 0, 5]

c = [-49, 58, 72, -78, 9, 65, -42, -3]
d = [30, -13, -70, 58, -34, 79, -36, 27]


#print(assign_mice_2_holes(a, b))
print(assign_mice_2_holes(c, d))
#print(assign_mice_2_holes([0], [55]))