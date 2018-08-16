# Created on Fri Sep  9 22:57:09 2016  ||  @author: axhufield


def frog(X, Y, D):
    import math
    return int(math.ceil((Y - X) / D))
    
print(frog(78, 85, 30))
print(frog(5, 105, 3))
