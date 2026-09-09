class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #given: an integer array nums 
        #return: all the triplets that equal to zero 
        #solution: First we can sort the array, we start with two pointers, at the initial and ending points 
        #we can also have a middle pointer, at each combo if we need either bigger than max or smaller than min 
        #then either move left or right pointer, otherwise find it and move left 

        nums.sort()
        valid = []

        for i in range(len(nums)-2): 
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]: 
                continue 

            if nums[i] > 0: 
                break
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r: 
                total = nums[i] + nums[l] + nums[r]
                if total < 0: 
                    l += 1
                elif total > 0: 
                    r -= 1
                else: 
                    valid.append([nums[i],nums[l],nums[r]])
                    r -= 1 
                    l += 1
                
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1
                    while l < r and nums[r] == nums[r+1]: 
                        r -= 1

                
        return valid

            




                        




        



        