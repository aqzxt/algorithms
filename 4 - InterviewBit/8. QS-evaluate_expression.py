"""
Created on Thu Apr  5 10:30:22 2018 ----------- @author: mxhfield
"""

def evaluate_expression(A):
    if len(A) == 1: return int(A[0])
    stack = []
    while A:
        stack.append( A.pop() )
        
        if len(stack) > 2:
            if not stack[-3][-1].isdecimal() and stack[-2][-1].isdecimal() and stack[-1][-1].isdecimal():
                if stack[-3] == '*': A.append( str(int(stack[-1]) * int(stack[-2])) )
                if stack[-3] == '/':
                    if stack[-2] == '0': A.append('0')
                    else: A.append( str(int(stack[-1]) // int(stack[-2])) )
                if stack[-3] == '+': A.append( str(int(stack[-1]) + int(stack[-2])) )
                if stack[-3] == '-': A.append( str(int(stack[-1]) - int(stack[-2])) )
                stack.pop(); stack.pop(); stack.pop()
                
        if len(A) == 1 and not stack: return int(A[0])


a = ["2", "1", "+", "3", "*"] # ((2 + 1) * 3) == 9
b = ["4", "13", "0", "/", "+"] # (4 + (13 / 5)) == 6
c = [ "-500", "-10", "/" ]

print(evaluate_expression(c))