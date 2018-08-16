"""
Created on Sat Feb 17 06:15:10 2018 ----------- @author: mxhfield

Suppose we had a list of n integers sorted in ascending order.
How quickly could we check if a given integer is in the list? 

"""

def binary_search(num, lst):
    lst.sort()
    lo = 0
    hi = len(lst)-1
    mid = len(lst)//2
    
    while lo < hi:
        if lst[mid] == num:
            return 'Success'
        if num < lst[mid]:
            hi = mid -1
            mid = mid //2
        else:
            lo = mid +1
            mid += (hi - mid+1) //2
    return 'Failure'
    

lst = [2,5,3,7,45,27,93,1,32,43,7,1,18,7]
print(binary_search(44, lst))  