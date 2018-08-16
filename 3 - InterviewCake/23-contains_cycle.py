"""
Created on Sun Feb 25 17:47:05 2018 ----------- @author: mxhfield
"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None
        
    def contains_cycle(node):
        
        after = node.next
        after_after = node.next.next
        
        while after.next is not None and after_after is not None:
            if node is after or node is after_after:
                return True
            
            after = after.next
            after_after = after_after.next
        return False

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')

a.next = b
b.next = c
c.next = d
#d.next = a


print(LinkedListNode.contains_cycle(b))
            

def contains_cycle(first_node):

    # start both runners at the beginning
    slow_runner = first_node
    fast_runner = first_node

    # until we hit the end of the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # case: fast_runner is about to "lap" slow_runner
        if fast_runner is slow_runner:
            return True

    # case: fast_runner hit the end of the list
    return False
