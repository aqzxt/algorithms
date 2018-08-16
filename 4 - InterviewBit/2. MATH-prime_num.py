"""
Created on Tue May 15 15:48:21 2018 ----------- @author: mxhfield
"""

from math import sqrt

def primes(A):
    '''Numbers only divisible by themselves and 1.
    '''
    primes = []
    for k in range(1,A+1):
        flag = True
        for i in range(2, int(sqrt(k)+1)):
            
            # when item is divisible by more: NOT a prime
            if k % i == 0: flag = False
        
        # if it is append it
        if flag: primes.append(k)
    return primes


print(primes(10))