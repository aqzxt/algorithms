"""
Created on Fri Feb 23 21:27:40 2018 ----------- @author: mxhfield
"""

class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)
        
    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            raise Exception('Empty stack')
        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item to the top of our stack."""
        self.stack.push(item)

        # If the item is greater than or equal to the last item in maxes_stack,
        # it's the new max! So we'll add it to maxes_stack.
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxes_stack.peek()
    




class Stack2:
    '''For PythonTutor.com visualization'''
    def __init__(self):
        self.stack = []
        self.maxes_stack = []
    def push(self, item):
        self.stack.append(item)
        if not len(self.maxes_stack) or item >= self.maxes_stack[-1]:
            self.maxes_stack.append(item)
    def pop(self):
        if not len(self.stack):
            return None
        item = self.stack.pop()
        if len(self.maxes_stack):
            if item == self.maxes_stack[-1]:
                self.maxes_stack.pop()
        return item

s = Stack2()
s.push(29)
s.push(45)
s.push(14)
s.push(81)
s.push(-3)
s.push(-42)
s.push(-20)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()