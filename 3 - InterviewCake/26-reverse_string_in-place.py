"""
Created on Mon Feb 26 03:41:13 2018 ----------- @author: mxhfield
"""

def reverse_string_in_place(word):
    chars = [e for e in word]
    for k in range(len(chars)//2):
        chars[k], chars[len(chars)-1-k] = chars[len(chars)-1-k], chars[k]
    return ''.join(chars)
    
    

word = 'keyboardinterrupt'

print(reverse_string_in_place(word))

