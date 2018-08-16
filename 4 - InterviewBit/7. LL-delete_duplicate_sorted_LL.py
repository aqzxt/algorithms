"""
Created on Wed Apr  4 03:41:07 2018 ----------- @author: mxhfield
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def deleteDuplicates(self, A):
        current = A
        right = A.next
        if not current: return
        if right is None: return A
            
        while right is not None:
            if current.val != right.val:
                current = right
                right = current.next
                
            elif right is not None:
                right = right.next
        return