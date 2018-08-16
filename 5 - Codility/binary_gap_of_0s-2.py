# Created on Thu Sep  8 19:37:06 2016  ||  @author: axhufield

def binaryGap(N):
    '''
    A binary gap within a positive integer N is any maximal sequence
    of consecutive zeros that is surrounded by ones at both ends
    in the binary representation of N.
    '''
    count = 0
    ans = 0
    binLen = len('{0:b}'.format(N))
    
    if N < 0 or len('{0:b}'.format(N)) < 3:
        return 0
    
    inc = 2
    
    while inc < binLen:
        if '{0:b}'.format(N)[inc -2] == '1' and '{0:b}'.format(N)[inc -1] == '0':
            count += 1
            
            while '{0:b}'.format(N)[inc] == '0':
                count += 1
                inc += 1
                if inc >= binLen:
                    break
            
            if inc +1 <= binLen:
                if '{0:b}'.format(N)[inc] == '1' and count > ans:
                    ans = count
                
            count = 0
        inc += 1
    
    print('{0:b}'.format(N))
    return ans

print(binaryGap(5))
