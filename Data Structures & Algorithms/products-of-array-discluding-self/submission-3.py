class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #given: An integer array  
        #return: An array where a specific index in that array is the product of all the elements besides that index
        #solution: should use the fact that we get to know the product of every other number in the array 
        #results[i] = results[i-1] * results[i+1]

        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(1, n): 
            res[i] = res[i-1] * nums[i-1]
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1): 
            res[i] *= suffix
            suffix *= nums[i]

        return res
