"""
Created on Sat Mar 10 04:33:30 2018 ----------- @author: mxhfield
"""

def atoi_str_2_int(A):
    if not A:
        return 0
    if not A[0].isdigit() and not A[0] in '+-':
        return 0
    
    answer = ''
    for k in A:
        if k in '+-':
            continue
        if k.isdigit():
            answer += k
        else:
            break
        
    if answer[0] == '0':
        i = 0
        for e in range(len(answer)):
            if answer[e] == 0:
                i = e
            else:
                break
        answer = answer[i+1:]
    
    if A[0] == '-':
        if -int(answer) < -2147483648:
            return '-' + '2147483648'
        else:
            return '-'+ str(answer)
            
    if int(answer) > 2147483647:
        answer = 2147483647

    return answer

a = "-54332872018247709407 4 54"
print(atoi_str_2_int(a))
print(atoi_str_2_int("9 2704"))

MAX_INT = 2**31 - 1
MIN_INT = -2**31

# @param A : string
# @return an integer
def atoi2(A):
    
	    # Remove whitespace
	    A = A.strip()
	    i, n = 0, len(A)
	    
	    # Handle sign
	    sign = 1
	    if A[0] == '-':
	        sign = -1
	    if A[0] in '-+':
	        i += 1
	    
	    # Process digits
	    res = 0
	    while i<n:
	        if '0' <= A[i] <= '9':
	            res = 10*res + (ord(A[i]) - 48)
	        else:
	            break
	        i += 1
	    
	    res = sign*res
	    
	    # Make python as dumb as C
	    return max(MIN_INT, min(MAX_INT, res))
