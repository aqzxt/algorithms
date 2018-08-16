"""
Created on Mon Feb 19 07:24:41 2018 ----------- @author: mxhfield

"""

def perm_palindrome(word):
    counter = {}
    for k in word:
        if counter.get( k ) is None:
            counter[k] = 1
        else:
            counter[k] += 1
    
    odd_letter_count = 0
    for k in counter.values():
        if k % 2 == 1:
            odd_letter_count += 1
            
    return odd_letter_count <= 1
    
word_list = ['racecar', 'civic', 'ivicc', 'civil', 'livci']
#result = [k for k in map(perm_palindrome, word_list)]
#print(result)

print(perm_palindrome('livci'))

def has_palindrome_permutation(the_string):
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    return len(unpaired_characters) <= 1

print(has_palindrome_permutation('livci'))