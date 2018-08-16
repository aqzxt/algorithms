"""
Created on Thu Feb 22 23:50:00 2018 ----------- @author: mxhfield
"""

def find_rotation_point(words):
    hi = len(words)-1
    lo = 0
    mid = len(words)//2
    
    while lo -1 < hi +1:
        if words[mid] > words[mid +1]:
            return mid +1
        
        if words[mid -1] > words[mid]:
            return mid
        
        if words[mid] < words[mid//2]:
            hi = mid
            mid = mid//2
        else:
            lo = mid
            mid += (hi - lo)//2
    return None
    
words = ['engender',
        'karpatka',
        'othellolagkage',
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'zenith',
        'zao',
        'asymptote',
        'babka',
        'banoffee']

print(find_rotation_point(words))