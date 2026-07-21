class Solution:
    #returning values instead of indices
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #pretty much, first sort the array, then go through each number, and if it's not equal to the prior
        #then perform two sum II on the rest of the list to equal -of the curr number 

        triples = []
        nums.sort()

        for index, val in enumerate(nums): 
            if index > 0 and val == nums[index-1]: 
                continue 
            target = -(val)
            left = index + 1 
            right = len(nums) - 1
            while left < right: 
                if nums[left] + nums[right] == target: 
                    triples.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                elif nums[left] + nums[right] < target: 
                    left += 1
                else: 
                    right -= 1
        return triples





        
        