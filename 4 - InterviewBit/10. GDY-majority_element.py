"""
Created on Thu Apr 12 12:55:07 2018 ----------- @author: mxhfield

Given an array of size n, find the majority element. The majority element is the element
that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist
in the array.

EXAMPLE:
Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""

    # @param A : tuple of integers
    # @return an integer
def majority_element(A):
    c = {}
    for k in A:
        if c.get(k) == None:
            c[k] = 1
        else:
            c[k] += 1
    target = len(A) //2
    for i in A:
        if c[i] > target:
            return i
        
