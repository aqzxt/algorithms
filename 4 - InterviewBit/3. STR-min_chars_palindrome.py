"""
Created on Fri Mar  9 00:44:33 2018 ----------- @author: mxhfield
"""

def min_chars_palindrome(A):
    left, right, count = 0, len(A)-1, len(A)-1
    
    while left <= right:
        
        if A[left] == A[right]:
            left += 1
            right -= 1
            
        else:
            left = 0
            right = count -1
            count -= 1
                
    return len(A)-count-1


def solve(s):
    s = s[::-1]
    for i in range(0,len(s)):
        s1 = s[i:]
        s2 = s1[::-1]
        print(s1, s2)
        if s1 == s2:
            break
        return i

#print(min_chars_palindrome('banana'))
#print(min_chars_palindrome('hqghumeaylnlfdxfi'))
#print(min_chars_palindrome('AACECAAAA'))
#print(min_chars_palindrome('abc'))
#print(min_chars_palindrome('lzyl'))

print(solve('hqghumeaylnlfdxfi'))