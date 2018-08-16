"""
Created on Thu May 10 19:11:40 2018 ----------- @author: mxhfield
"""


def rev_int(A):
    pos = 2147483647
    neg = -2147483646
    s = str(A)[::-1]
    if A < 0:
        s = '-' + s[:-1]
    A = int(s)
    if A < neg or A > pos:
        return 0
    return s
    
print(rev_int(-81328070))