"""
Created on Wed Apr  4 17:52:44 2018 ----------- @author: mxhfield
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def rotateRight(A, B):
        current = A
        right = A.next
        if not right: return A.val
        
        order = []
        while right is not None:
            order.append(current)
            current = right
            right = right.next
        order.append(current)
        
        n = len(order)
        if B > n:
            B = B%n
        
        new_tail = order[-B-1]
        A = new_tail.next
        new_tail.next = None
        
        inter = order[-1]
        inter.next = order[0]
        
        
        for k in range(n):
            if k +1 == n:
                print(order[(-B+k)%n].val, end=' ')
            else:
                print(order[(-B+k)%n].val, end=' -> ')
        return ''




head = ListNode(1)
A = head
for k in range(2,20):
    new = ListNode(k)
    head.next = new
    head = new
    
head.next = None
    

print(Solution.rotateRight(A, 50))



