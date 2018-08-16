"""
Created on Fri Mar  9 05:57:21 2018 ----------- @author: mxhfield
"""

def roman_to_int(A):
    roman = {
    'I':1, 'II':2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9, 'X':10,
    'XX':20, 'XXX':30, 'XL':40, 'L':50, 'LX':60, 'LXX':70, 'LXXX':80, 'XC':90, 'C':100,
    'CC':200, 'CCC':300, 'CD':400, 'D':500, 'DC':600, 'DCC':700, 'DCCC':800,
    'CM':900, 'M':1000
    }
    
    answer = 0
    left, right, flag = 0, len(A)+1, False
    if right > 4:
        right = 4
        
    while left < len(A):
        while left <= right:
            
            if A[left:right] in roman:
                answer += roman.get( A[left:right] )
                flag = True
                break
            right -= 1
            
        if flag:
            left = right
            flag = False
        else:
            left += 1
        
        if len(A[left:]) >= 4:
            right += 4
        else:
            right += len(A[left:])
#        print(len(A[left:]), A[left:right])
    return answer

#print(roman_to_int('MDCCCIV'))
#print(roman_to_int('MMCDLXXV'))


    # @param A : string
    # @return an integer
def romanToInt(A):
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    # The last letter always gets added
    _sum = roman[A[-1]]
    # Iterate over A in pairs of two
    for x, y in zip(A[:-1], A[1:]):
        current, _next = roman[x], roman[y]
        print(current, _next, _sum)
        # If pair is like IV
        if current < _next:
            _sum -= current
        # Else if like VI
        else:
            _sum += current
    return _sum

print(romanToInt('MMCDLXXV'))