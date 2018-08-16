"""
Created on Sat Apr 14 16:51:30 2018 ----------- @author: mxhfield
"""
from functools import cmp_to_key

def highest_product_3(A):
    if len(A) == 3: return A[0]*A[1]*A[2]
    a = max(A); a_index = A.index(a); A[a_index] = 0
    
    if a < 0:
        k = cmp_to_key(lambda a,b: 1 if a < b and not b else -1)
        d = max(A, key=k); d_index = A.index(d); A[d_index] = 0
        e = max(A, key=k)
        return a*d*e
    
    b = max(A); b_index = A.index(b); A[b_index] = 0
    c = max(A)
    
    k = cmp_to_key(lambda a,b: 1 if a < b else -1)
    d = max(A, key=k); d_index = A.index(d); A[d_index] = 0
    e = max(A, key=k)
    
    x = a*b*c; y = a*d*e
    if not d or not e or x > y: return x
    return y

def h2(A):
    A.sort(reverse = True)
    return max(A[0]*A[1]*A[2] , A[0]*A[-1]*A[-2])


a = [-40, -15, -49, -17, -8, -39, 86, -43, 47, 25, 58, -35, -38, -87, -11, 1, -13, -73, -24, 72, 31, 40, 5, -16, -32, 96, 69, 54, -23]
b = [-81, -94, 19, -44, 85, -91, -11, -46, -18, -18, 89, 48, -16, 22, 21, -94, -51, 64, 99, -47, 76, 63, -82, -72, 20, 56, -67, 81, 16, 47, 63, 36, 27, -78, -78]

#print(highest_product_3([0, -1, 3, 100, -70, -50]))     # 350000
#print(highest_product_3([-10000000, 1, 2, 3, 4]))       # 24
#print(highest_product_3([-1, -2, -3, -4, -5]))          # -6
#print(highest_product_3([5, 5, 5, -1, -1]))             # 125
#print(highest_product_3([0, -1, -2, -3]))               # 0
#print(highest_product_3([1, 3, 5, 2, 8, 0, -1, -3]))    # 120
#print(highest_product_3(a))                             # 609696
#print(highest_product_3(b))                             # 874764

print(h2([0, -1, 3, 100, -70, -50]))     # 350000
print(h2([-10000000, 1, 2, 3, 4]))       # 24
print(h2([-1, -2, -3, -4, -5]))          # -6
print(h2([5, 5, 5, -1, -1]))             # 125
print(h2([0, -1, -2, -3]))               # 0
print(h2([1, 3, 5, 2, 8, 0, -1, -3]))    # 120
print(h2(a))                             # 609696
print(h2(b))                             # 874764