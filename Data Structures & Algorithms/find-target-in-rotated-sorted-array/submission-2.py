class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #given: the rotated sorted array nums 
        #return: the index of target
        #use binary search 
        #if the middle point is greater than the target, then there are 2 possible situations: 
        #1. the target is to the left but the right point is greater
        #2. the target is to the right 
        bot = 0 
        top = len(nums) - 1
        start = 0 

        while bot <= top: 
            mid = bot + (top-bot)//2
            if nums[mid] == target: 
                return mid

            #left sorted portion
            if nums[bot] <= nums[mid]: 
                if target > nums[mid] or nums[bot] > target : 
                    bot = mid + 1
                else: 
                    top = mid - 1

            #right sorted portion
            else: 
                if target < nums[mid] or target > nums[top]: 
                    top = mid - 1 
                else: 
                    bot = mid + 1
        return -1
            
        