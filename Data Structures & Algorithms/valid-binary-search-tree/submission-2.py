# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #given: root of a binary tree
        #return: whether it is a valid binary search tree
        #use dfs for this one and a recursive approach in which you check wehether each child is a bst with 
        #base case of it having no children

        def isValidSubtree(node, left, right): 
            if not node: 
                return True 
            if node.val <= left or node.val >= right: 
                return False
            return (isValidSubtree(node.left, left, node.val) and isValidSubtree(node.right, node.val, right))
        
        return isValidSubtree(root, float("-inf"), float("inf"))
