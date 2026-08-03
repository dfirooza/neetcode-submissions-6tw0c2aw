# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #classic bfs 
        if root is None: 
            return []
        results = []
        queue = collections.deque([root])
        while queue: 
            level_length = len(queue)
            curr_level = []
            for i in range(level_length): 
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            results.append(curr_level)
        return results



            
        