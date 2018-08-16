"""
Created on Thu Mar  8 22:51:30 2018 ----------- @author: mxhfield
"""
def reverseWords(A):
    ans = ''
    s = A.split()
    for e in s[::-1]:
        ans += e + ' '
    return ans[:-1]
    
def reverseWords2(A):
    words = A.split(" ")
    words.reverse()
    ans=" ".join(words)
    return ans

def reverseWords3(A):
    arr=A.split(" ")
    arr2=reversed(arr)
    return " ".join(arr2)

def reverseWords4(A):
    i = len(A)-1
    S = ''
    while i >= 0:
        while i >= 0 and A[i] == ' ':
            i -= 1
        S += ' '
        j = i
        
        while j >= 0 and A[j] != ' ':
            j -= 1
        
        S += A[j+1:i+1]
        i = j
        
    S = S.strip()
    return S