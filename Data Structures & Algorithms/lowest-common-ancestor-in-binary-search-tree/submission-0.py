# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """def latest(paths):
        lca = 0 
        seen = set()
        for i in min(paths): 
            seen.append(i)
        for j in max(paths): 
            if j in seen: 
                lca = j
        return lca"""
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        else: 
            return root
        """paths = []
        curr = []
        if self.val == p.val or self.val == q.val: 
            paths.append(curr)
            if len(paths) == 2: 
                return latest(paths)
            else: 
                return self.lowestCommonAncestor(root, p, q)
        else: 
            curr.apend(self.val)"""
        

        