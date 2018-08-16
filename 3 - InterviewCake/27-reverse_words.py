"""
Created on Mon Feb 26 04:06:05 2018 ----------- @author: mxhfield
"""
import time

def reverse_words(A):
    
    start = time.clock()
    
    def rev_chars(A, a, b):
        while a < b:
            A[a], A[b] = A[b], A[a]
            a += 1
            b -= 1
    
    
    A = list(A)
    e, k = 0, len(A)-1
    a, d = e, k
    while e < k:
        A[e], A[k] = A[k], A[e]
        
        if A[e] == ' ':
            b = e-1
            rev_chars(A, a, b)
            a = b+2
            
        if A[k] == ' ':
            c = k+1
            rev_chars(A, c, d)
            d = c-2
            
        e += 1
        k -= 1
#        print(''.join(A))
    
    if A[a].isalpha():
        rev_chars(A, a, d)
        
    end = time.clock()
    return ''.join(A), end - start



def reverse_words3(A):
    s = time.clock()
    A = list(A)
    e, k = 0, len(A)-1
    a, d = e, k
    while e < k:
        A[e], A[k] = A[k], A[e]
        
        if A[e] == ' ':
            b = e-1
            bak = b
            while a < b:
                A[a], A[b] = A[b], A[a]
                a += 1
                b -= 1
            a = bak+2
            
        if A[k] == ' ':
            c = k+1
            bak = c
            while c < d:
                A[c], A[d] = A[d], A[c]
                c += 1
                d -= 1
            d = bak-2
            
        e += 1
        k -= 1
        
#        print(''.join(A))
    
    if A[a].isalpha():
        while a < d:
            A[a], A[d] = A[d], A[a]
            a += 1
            d -=1
    f = time.clock()
    return ''.join(A), f - s
        
    




def reverse_words2(message):
    start = time.clock()
    
    message = list(message)
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backwards

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1
    end = time.clock()
    return ''.join(message), end - start


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1


msg = 'find you will pain only go you recordings security the into if'

print(reverse_words(msg))
print(reverse_words3(msg))
print(reverse_words2(msg))