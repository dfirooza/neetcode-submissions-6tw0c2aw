class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0 
        best_total = 0
        if len(nums) == 1: 
            return nums[0]
        for index, val in enumerate(nums): 
            total += val
            if total <= 0: 
                total = 0 
            best_total = max(total, best_total)
        if max(nums) < 0: 
            return max(nums)
        else: 
            return best_total