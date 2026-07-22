# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isValid(self, root, subRoot): 
        if root == None and subRoot == None: 
            return True
        elif root == None or subRoot == None: 
            return False 
        if root.val == subRoot.val: 
            return self.isValid(root.left, subRoot.left) and self.isValid(root.right, subRoot.right)
        else: 
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # root is above subRoot 
        #first traverse root until you find a node/nodes that equal to the root of subRoot, then just run the algorithm from before 
        if root == None: 
            return False
        if root.val != subRoot.val: 
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else: 
            if self.isValid(root, subRoot): 
                return True
            else: 
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
