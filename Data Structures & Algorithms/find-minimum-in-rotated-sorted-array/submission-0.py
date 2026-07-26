class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the min will always be either a. the first index of the list or b. right after the max element
        bot = 0 
        top = len(nums) - 1
        while bot < top: 
            mid = bot + (top-bot)//2
            if nums[mid] > nums[top]: 
                bot = mid + 1
            else: 
                top = mid
        return nums[bot]
