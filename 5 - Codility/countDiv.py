# Created on Sat Sep 10 22:15:35 2016  ||  @author: axhufield


def countDiv(A, B, K):
    count = 0
    for e in range(A, B+1):
        if e % K == 0:
            count += 1
    return count
    
def countDiv2(A, B, K):
    count = 0
    if A == B:
        return 0
    if A % K == 0:
        count += 1
    return count + countDiv2(A+1, B, K)
    
print(countDiv(11, 345, 17))
