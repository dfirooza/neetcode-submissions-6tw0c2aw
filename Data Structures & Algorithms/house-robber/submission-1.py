class Solution:
    def rob(self, nums: List[int]) -> int:
        #goal: given an integer array nums where nums[i] represents the amount of money the ith house has
        #return: max amount of money you can rob
        rob1, rob2 = 0, 0 

        for num in reversed(nums): 
            rob1, rob2 = rob2, max(num + rob1, rob2)
        return rob2


