"""
Created on Thu Mar  8 19:00:59 2018 ----------- @author: mxhfield
"""

def prettyPrint(num):
    dec = [e for e in range(num, 0, -1)]
    lists = []
    
    for k in range(num, 0, -1):
        to_add = dec
        
        '''The importance of PROPER DEBUGGING:
            
        a = [w for w in range(num, -1, -1)]
        b = [q for q in range(num-k, num)]
        
        print(a, b)
        '''
        for e in range(num-k, num):
            to_add[e] = k
            
        to_add = to_add[:-1] + to_add[::-1]
        lists.append(to_add)
        
    c = lists[::-1]
    lists += c[1:]
    
    for e in lists:
        print(e,)
    
    return ''

    
print(prettyPrint(5))