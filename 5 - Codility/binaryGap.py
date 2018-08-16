# Created on Thu Nov 10 01:00:39 2016 || @author: mxhfield

def biSearchGap(x):
    if x % 2 != 0:
        return False
    if x == 2:
        return True
    else:
        return biSearchGap(x / 2)
        

def binaryGap(N):
    '''
    Given a positive integer N, returns the length of its longest binary gap.
    The function should return 0 if N doesn't contain a binary gap
    '''
    gap = 0
    
    if biSearchGap(N) == True or biSearchGap(N +1) == True:
        return gap
    
    binary = "{0:b}".format(N)
    temp = 0
    inc = 1
    one = False
    
    while len(binary) > 0:

        if binary[0] == "1":
            one = True
            
        try:    
            if one and binary[inc] == "0":
                temp += 1
        except:
            break
            
        if binary[inc] == "1":
            if temp > gap:
                gap = temp
            temp = 0
            
        binary = binary[1:]
    return gap
    
print(biSearchGap(2147483647))
print(binaryGap(15))
            