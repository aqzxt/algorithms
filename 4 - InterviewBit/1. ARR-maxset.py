"""
Created on Tue Feb 27 19:42:44 2018 ----------- @author: mxhfield
"""

def maxset(A):
    answer = []
    sub = []
    
    for k in range(len(A)):
        if A[k] >= 0:
            sub.append(A[k])
        elif len(sub):
            answer.append(sub)
            sub = []
    
    if A[-1] > 0:
        answer.append(sub)
            
    if not len(answer):
        return ''
    
    len_greatest = 0
    sum_greatest = 0
    index = 0
    equal_sum_sub_index = 0
    
    for e in range(len(answer)):
        sum_each = sum(answer[e])
        len_each = len(answer[e])
        
        if sum_each > sum_greatest:
            sum_greatest = sum_each
            index = e
            
        if len_each > len_greatest:
            len_greatest = len_each
            
        if sum_each == sum_greatest:
            equal_sum_sub = sum_each
            equal_sum_sub_index = e
        
    if equal_sum_sub == sum_greatest:
        return answer[equal_sum_sub_index]
    return answer[index]

a = [3, 5, -7, 1, 2, 5]
b = [-1, -1, -1, -1, -1]
print(maxset(a))
