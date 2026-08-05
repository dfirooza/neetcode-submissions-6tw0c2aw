# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #given: the root of a binary search tree
        #return: the kth smallest value in the tree
        #solution: keep a stack and keep adding the smallest not seen node to it
        #once it reaches a length of k, pop from it and return that value
        #use inorder traversal

        result = []
        def dfs(node): 
            if not node: 
                return
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root) 
        return result[k-1]