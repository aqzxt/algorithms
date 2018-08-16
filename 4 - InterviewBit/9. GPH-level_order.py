"""
Created on Wed Apr 11 03:55:46 2018 ----------- @author: mxhfield
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

	# @param A : root node of tree
	# @return a list of list of integers
def levelOrder(A):
    d = {0: [A]}
    i = k = 0
    answer = [[A.val]]
    while True:
        k = i+1
        d[k] = []
        answer.append([])
        if d.get(i):
            for parent in d[i]:
                if parent.left is not None:
                    d[k].append(parent.left)
                    answer[k].append(parent.left.val)
                if parent.right is not None:
                    d[k].append(parent.right)
                    answer[k].append(parent.right.val)
            i = k
        
        else:
            del answer[-1]
            del answer[-1]
            break
    return answer

a = TreeNode(817)
b = TreeNode(91)
c = TreeNode(738)
#d = TreeNode(32)
#e = TreeNode(723)
#f = TreeNode(87)
#g = TreeNode(123)

#a.left = b
#a.right = c
#b.left = d
#b.right = e
#c.left = f
#c.right = g

print(levelOrder(a))