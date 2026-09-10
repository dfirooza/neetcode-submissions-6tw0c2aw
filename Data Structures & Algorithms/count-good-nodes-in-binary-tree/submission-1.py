# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import numpy as np

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #given: the root of a binary tree 
        #return: the number of good notes within the tree 
        #solution: recursively traverse left subtree once and right subtree once 
        #on each step just check if the current node is greater than the curr max 
        #along that path

        def dfs(node, max_val): 
            if not node: 
                return 0
            if node.val >= max_val: 
                max_val = node.val
                return 1 + dfs(node.left, max_val) + dfs(node.right, max_val)
            else: 
                return dfs(node.left, max_val) + dfs(node.right, max_val)
        
        return dfs(root, -np.inf)
        
        
        