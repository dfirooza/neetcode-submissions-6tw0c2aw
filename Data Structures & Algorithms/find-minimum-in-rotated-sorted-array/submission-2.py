class Solution:
    def findMin(self, nums: List[int]) -> int:
        #given: an array that was originally sorted in ascending order and is now rotated
        #return: minimum element of this array 
        #solution: you just need to find the point at which the previous number is greater and the next number is less, use binary search
        #[7,8,9,1,2,3,4,5,6]
         
        l, r = 0, len(nums) - 1 

        while l < r: 
            m = (l + r)//2

            #multiple specific cases
            if nums[m] > nums[r]:  
                l = m + 1
            else: 
                r = m
        return nums[l]
            

             




            
            
         