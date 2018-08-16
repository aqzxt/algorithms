"""
Created on Sat Mar 10 03:10:24 2018 ----------- @author: mxhfield
"""

def zigzag_string(A, B):
    if B == 1:
        return A
    if not B:
        return ''
    
    lines = []
    i = 0
    while i < B:
        lines.append([])
        i += 1
    
    zigzag = 0
    down = True
    for k in A:
        lines[zigzag].append(k)
        
        if down and zigzag +1 == B:
            zigzag -= 1
            down = False
            
        elif down:
            zigzag += 1
        
        elif not down and zigzag == 0:
            zigzag += 1
            down = True
            
        else:
            zigzag -= 1
    
    # alternative = ''.join([''.join(chars[i]) for i in range(len(chars))])
    answer = ''
    for k in lines:
        answer += ''.join(k)
        
    return answer

print(zigzag_string('PAYPALISHIRING', 3))