"""
Created on Wed Apr 18 18:18:04 2018 ----------- @author: mxhfield
"""

def seats(A):
    start = A.find('x'); end = A.rfind('x')
    if start == -1: return 0
    
    x_num = A.count('x'); c = 0
    for e in range(len(A)):
        if A[e] == 'x':
            c += 1
            if c == x_num//2+1:
                mid = e
                break
    
    mid_right = mid + A[mid:].index('.')
    mid_left = A[:mid+1].rindex('.')
    
    k = start+1; left = c = 0
    while k < mid_left+1:
        if A[k] == '.': c += 1
        else: left = left + c +1
        
        print(left,'['+str(A[k:mid_left+1])+']',c)
        k += 1
    
    k = end-1; right = c = 0
    while k > mid_right-1:
        if A[k] == '.': c += 1
        else: right = right + c +1
        
        print(right,'['+str(A[mid_right:k+1])+']',c)
        k -= 1
        
    print(left, right)
    return (left+right) % 10000003
    

a = '...xx.x..x..x'
b = '.x.x..x.x...x..x...x.x.'
print(seats(b))