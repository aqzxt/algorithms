"""
Created on Wed Mar 21 06:53:00 2018 ----------- @author: mxhfield
"""
import time

def num_range(A, B, C):
    start = time.clock()
    
    if not B and not C:
        if A[0] > 0:
            return 0
        return 1
    
    k = e = count = 0
    i=0
    while e < len(A):
        
        i+=1
        print(e, i, len(A))
        
        if B <= sum(A[e:k]) <= C:
            count += 1
            
        if k == len(A):
            e += 1
            k = e
            
        k += 1
    end = time.clock()
    return count, end - start


def num_range2(A, B, C):
    start = time.clock()
    if not B and not C:
        if A[0] > 0:
            return 0
        return 1
    
    k = e = count = 0
    i = 1
    while e < len(A):
        if i < len(A):
            A[i] += A[i-1]
            i += 1
        
        if A[k] == A[e] and B <= A[e] <= C:
            count += 1
        
        elif B <= A[k] - A[e] <= C:
            count += 1
        
        if k +1 == len(A):
            e += 1
            k = e-1
        
        k += 1
    end = time.clock()
    return count, end - start
    
    
        
a = [80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90]
b = [76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66]

#print(num_range([0], 0, 0))
print(num_range(a, 99, 269)) # 58
#print(num_range(b, 98, 290)) # 84
#print(num_range([10, 5, 1, 0, 2], (6, 8)))