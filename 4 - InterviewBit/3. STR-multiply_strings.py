"""
Created on Sat Mar 10 02:55:59 2018 ----------- @author: mxhfield
"""

def multiply_string(A, B):
    if not int(A) or not int(B):
        return 0
    return int(A) * int(B)

print(multiply_string('3', '98'))