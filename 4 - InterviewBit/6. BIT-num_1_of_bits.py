"""
Created on Fri Mar 30 22:11:11 2018 ----------- @author: mxhfield
"""

def num_set_bits(A):
    a = '{0:08b}'.format(A)
    c = 0
    for k in str(a):
        if k == '1':
            c += 1
    return c, a

#print(num_set_bits(-1))


def num_set_bits2(A):
    count = 0
    while A > 0:
        print(A)
        A &= A - 1
        count += 1
    return count

print(num_set_bits2(4))
    
    
def num_set_bits3(A):
    ans = 0
    for i in bin(A)[2:]:
        if i == '1':
            ans += 1
    return ans


def num_set_bits4(A):
    numbits = 0
    while A:
        numbits += int(A % 2 == 1)
        A = A/2
    return numbits