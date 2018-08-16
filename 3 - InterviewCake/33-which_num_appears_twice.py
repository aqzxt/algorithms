"""
Created on Mon Feb 26 06:19:33 2018 ----------- @author: mxhfield
"""

def which_num_appears_twice(array):
    ''' (n²+n)/2==total'''
    array.sort()
    for k in range(len(array)-1):
        if array[k] == array[k+1]:
            return array[k]
    return 0
    

array = [11,28,64,3,30,44,51,7,97,23,81,7,9,41,10]
#print(which_num_appears_twice(array))


def repeatedNumber1(A): # ?????????????????????????
    #convert the tuple to a list
    A = list(A)
    #traverse the array, make the number at the given index negative
    #if the number at the index is already negative, it has been encountered before
    for i in range(len(A)):
        m = abs(A[i])
        if A[m-1] < 0:
            return m
        else:
            A[m-1] = -A[m-1]
    return -1

print(repeatedNumber1(array))


def repeatedNumber2(A): # ?????????????????????????
    s = sum(A)
    n = len(A)
    missing = s - (n*(n-1))/2
    print(s, n, n-1, 2)
    return missing

print(repeatedNumber2(array))