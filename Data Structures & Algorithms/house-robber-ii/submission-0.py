class Solution:
    def rob(self, nums: List[int]) -> int:
        #only difference is that it's circular here
        #only difference with that is that you must check whether the first and last are neighbors
        #each time you are either robbing the current house or the house before 
        if len(nums) == 1: 
            return nums[0]

        def rob_linear(houses):
            rob1, rob2 = 0, 0 

            for num in houses:
                rob1, rob2 = rob2, max(num + rob1, rob2)
            return rob2
        
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))