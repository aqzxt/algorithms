"""
Created on Wed Apr  4 19:22:44 2018 ----------- @author: mxhfield
"""

S = 'IndexError: list index out of range'

def reverse_string_stack(A):
    stack = list(A); A = ''
    while stack: A += stack.pop()
    return A
    
    
print(reverse_string_stack(S))