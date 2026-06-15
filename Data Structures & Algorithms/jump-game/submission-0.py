class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0 
        for index, val in enumerate(nums): 
            if max_reachable >= len(nums): 
                return True
            if index > max_reachable: 
                return False 
            max_reachable = max(max_reachable, index + val)
        return True