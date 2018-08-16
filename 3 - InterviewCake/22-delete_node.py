"""
Created on Sun Feb 25 05:05:47 2018 ----------- @author: mxhfield
"""

class LinkedListNode:
    
    def __init__(self, value):
        self.value = value
        self.next  = None
        
    def delete_node(node): # b
        current = node
        
        old_b_next = current.next # c
        old_b_next = current
        current = current.next # a.next (b) = c
        current.value = old_b_next.value
        current.next = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

LinkedListNode.delete_node(a)
print('a ===',a)
print('a.value ===',a.value)
print('a.next ===',a.next)
print()
print('b ===',b)
print('b.value ===',b.value)
print('b.next ===',b.next)
print()
print('c ===',c)
print('c.value ===',c.value)
print('c.next ===',c.next)
print()