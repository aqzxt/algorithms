"""
Created on Wed Feb 28 22:42:03 2018 ----------- @author: mxhfield
"""
from itertools import permutations as perm

def largest_number(A):
    A = list(A)
    A.sort(key=str, reverse=True)
    largest, equals, k = '', [], 0
    
    while k < len(A):
        current = str(A[k])
        
        if k +1 < len(A):
            next = str(A[k +1])
        
            if current[0] == next[0]:
                equals.append(current)
            else:
                largest += current
                
        elif equals:
            prev = str(A[k-1])
            if prev[0] == current[0]:
                equals.append(current)
            
            equals = [e for e in perm(equals, len(equals))]
            biggest = ''
            for tup in equals:
                combination = ''.join(tup)
                if combination > biggest:
                    biggest = combination
            largest += biggest
            equals = []
            
        else:
            largest += current
        
        
        k += 1
    return largest
    
a1 = [12, 121]
a2 = [3, 30, 34, 5, 9, 310]
a3 = [8, 89]
a4 = [980, 674, 250, 359, 98, 969, 143, 379, 363, 106, 838, 923, 969, 880, 997, 664, 152, 329, 975, 377, 995, 943, 369, 515, 722, 302, 496, 124, 692, 993, 341, 785, 400, 113, 302, 563, 121, 230, 358, 911, 437, 438, 494, 599, 168, 866, 689, 444, 684, 365, 470, 176, 910, 204, 324, 657, 161, 884, 623, 814, 231, 694, 399, 126, 426]
#print(largest_number(a4))





from functools import cmp_to_key

def largestNumber1(A):
    ''' When comparing numbers we must pick the one leading
        to the best concatenated result:
            787978 > 787879  so 7879 is 'bigger' than 78
                        but     7879 is 'less' than 788
    '''
    
    # Convert to string once, for proper comparison a+b vs b+a
    A = map(str, A)
    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
    result = ''.join(sorted(A, key= key, reverse=True))
    # Must left trim 0, apparently
    result = result.lstrip('0')
    return result if result else '0'

print(largestNumber1(a2))


def largestNumber2(A):
    maxlen = len(str(max(A)))
    if all(v == 0 for v in A):
        return '0'
    return ''.join(sorted((str(v) for v in A), reverse=True, key=lambda i: i*(maxlen * 2 // len(i))))



def largestNumber3(A):
    A = list(A)
    def partiation(A, start, end):
        pivot = A[end]
        pindex = start
        for i in range(start, end):
            flag =False
            curr = str(A[i])
            piv = str(pivot)
            if int(curr+piv)>int(piv+curr):
                flag = True
            if flag:
                A[i], A[pindex] = A[pindex], A[i]
                pindex += 1
        A[end], A[pindex] = A[pindex], A[end]
        return pindex

    def quickSort(A, start, end):
        if start < end:
            pindex = partiation(A, start, end)
            quickSort(A, start, pindex - 1)
            quickSort(A, pindex + 1, end)
        return A

    xxx = quickSort(A, 0, len(A) - 1)
    yyy = ""
    for i in xxx:
        if i != 0 or yyy:
            yyy+=str(i)
    if not yyy:
        return "0"
    return yyy
