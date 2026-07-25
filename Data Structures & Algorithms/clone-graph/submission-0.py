"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #use a seen set and a queue
        #we don't want to explore a node that we've already explored
        #once we explore a node we add its neighbors to a queue (set) and explore that in order popping each time we explore
        #during an exploratin of a node we add its neighbors to a list and add that to our result
        #the base case is when our queue is empty
        #misunderstood this q, we just need to create a deep copy
        
        oldToNew = {}

        def dfs(node): 
            if node in oldToNew: 
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors: 
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node) if node else None
        #need the first number in the queue that hasn't already been explored


        
        
        