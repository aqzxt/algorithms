"""
Created on Mon Feb 26 02:16:42 2018 ----------- @author: mxhfield
"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        
    def reverse(head):
        after = head.next.next
        while 1:
            
            head.next.next = head                # re-assign next node to head
            head = after.next.next          # track current node
            after = head.next
            
            if after.next is None:
                break      
            
            
a, b, c, d, e, f = LinkedListNode('A'), LinkedListNode('B'), LinkedListNode('C'), \
                    LinkedListNode('D'), LinkedListNode('E'), LinkedListNode('F')
a.next, b.next, c.next, d.next, e.next = b, c, d, e, f

LinkedListNode.reverse(a)
print('a ===',a)
print('a.next ===',a.next)
print()
print('b ===',b)
print('b.next ===',b.next)
print()
print('c ===',c)
print('c.next ===',c.next)
print()
print('d ===',d)
print('d.next ===',d.next)
print()
print('e ===',e)
print('e.next ===',e.next)
print()
print('f ===',f)
print('f.next ===',f.next)
print()
