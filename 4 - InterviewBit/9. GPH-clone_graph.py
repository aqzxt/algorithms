"""
Created on Thu Apr 12 02:21:32 2018 ----------- @author: mxhfield
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

from copy import deepcopy as dc

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        cloned = []; s = set()
        new = dc(node)
        
        for k in new.neighbors:
            tmp = dc(k)
            tmp.neighbors = k.neighbors[:]
            cloned.append(tmp)
            s.add(tmp)
        
        flag = False
        cloned.append(new)
        while 1:
            for i in cloned:
                if i not in s:
                    for j in i.neighbors:
                        tmp = dc(j)
                        tmp.neighbors = j.neighbors[:]
                        cloned.append(tmp)
                        s.add(tmp)
                    flag = False
            if flag:
                break
            flag = True
            
        return cloned[0]
   

    level = [s]                        # first level includes only s
    while len(level) > 0:
        next_level = []                  # prepare to gather newly found vertices
        for u in level:
            for e in g.incident_edges(u):  # for every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:      # v is an unvisited vertex
                    discovered[v] = e          # e is the tree edge that discovered v
                    next_level.append(v)       # v will be further considered in next pass
        level = next_level