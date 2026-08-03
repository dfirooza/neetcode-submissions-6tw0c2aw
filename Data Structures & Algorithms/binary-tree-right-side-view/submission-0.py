# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #given: the root of a binary tree 
        #return: only the values of the nodes that are visible from the right side of the tree
        #solution: go through each level and seaparate for each level the nodes on the left side of the tree 
        #from those on the right 
        #add all the right ones for a row, but if there's no right ones then add the left ones

        if not root: 
            return []
        
        res = []
        q = collections.deque([root])

        while q: 
            level_length = len(q)
            for i in range(level_length): 
                node = q.popleft()
                if i == (level_length - 1): 
                    res.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
        return res

        
 

                    
                

        