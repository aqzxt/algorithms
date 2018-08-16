"""
Created on Fri Mar  9 04:00:24 2018 ----------- @author: mxhfield
"""

def isPalindrome(A):
    pal = []
    for k in A:
        if k.isalpha():
            if k.isupper():
                k = k.swapcase()
            pal.append(k)
        if k.isdigit():
            return 0
    
    if len(pal) == 1:
        return 1
    
    left, right = 0, len(pal)-1
    while left < right:
        if pal[left] != pal[right]:
            return 0
        left += 1
        right -= 1
    
    return 1


print(isPalindrome('A man, a plan, a canal: PanamaZ'))