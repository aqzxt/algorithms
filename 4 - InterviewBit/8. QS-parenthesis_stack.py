"""
Created on Thu Apr  5 01:20:22 2018 ----------- @author: mxhfield
"""

def parenthesis_stack(A):
    if len(A) < 2: return 0
    stack = [A[0]]
    for k in range(1, len(A)):
        if not stack:
            stack.append(A[k])
        elif (stack[-1] == '(' and A[k] == ')') or \
            (stack[-1] == '[' and A[k] == ']') or \
            (stack[-1] == '{' and A[k] == '}'):
                stack.pop()
        else:
            stack.append(A[k])
    if len(stack):
        return 0
    return 1

a = "((((([{()}[]]{{{[]}}})))))"
b = '()[]{}'

print(parenthesis_stack(b))