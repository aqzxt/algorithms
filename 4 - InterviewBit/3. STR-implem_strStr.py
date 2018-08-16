"""
Created on Sat May 19 18:02:49 2018 ----------- @author: mxhfield
"""

def strStr(A, B):
    # if both needle and/or haystack are empty OR A is bigger than B
    if not B or len(B) > len(A): return -1
    # if only haystack is empty
    if not A: return B
    
    i = 0
    while i < len(A):
        
        # first letter match found
        if A[i] == B[0]:
            index = i
            
            # if length of A -i is less than B
            if len(A) -i < len(B):
                return -1
            
            k = 0
            match = True
            while k < len(B):
                if A[i] != B[k]:
                    match = False
                    break
                i += 1
                k += 1
            
            # success
            if match:
                return index
            else:
                i = index +1
            
        
        # if different, increment i
        else:
            i += 1
            
    # unsuccessuful search
    return -1


A = "bbbbbbbbab"
B = "baba"

C = 'bababaaaabbbbbaaababbbbaabbbbaabbabaabbaababaabbabbbbbbbaba'
D = 'abbaaabaaabbaaabbabaaabbabbababaaaaaaa'
print(strStr(C, D))
print(strStr('cabe', 'be'))