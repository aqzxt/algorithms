# Created on Thu Sep  8 19:37:06 2016  ||  @author: axhufield


def solution(N):
    '''
    A binary gap within a positive integer N is any maximal sequence
    of consecutive zeros that is surrounded by ones at both ends
    in the binary representation of N.
    '''
    count = 0
    ans = 0
    bigger = 0
    if N < 0:
        return 0
    for e in '{0:b}'.format(N):
        if e == '0':
            count += 1
            ans = count
        if ans > bigger:
            bigger = ans
        if e == '1':
            count = 0
    print('{0:b}'.format(N))
    return bigger
    

print(solution(51712))
