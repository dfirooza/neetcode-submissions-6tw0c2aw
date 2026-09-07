class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #given: An integer array  
        #return: An array where a specific index in that array is the product of all the elements besides that index
        #solution: should use the fact that we get to know the product of every other number in the array 
        #results[i] = results[i-1] * results[i+1]

        n = len(nums)

        prefixes = [1] * n
        suffixes = [1] * n
        values = [1] * n

        for i in range(1, n): 
            prefixes[i] = prefixes[i-1] * nums[i-1]

        for i in range(n-2, -1, -1): 
            suffixes[i] = suffixes[i+1] * nums[i+1]
        
        for i in range(len(nums)): 
            values[i] = prefixes[i] * suffixes[i]
        
        return values
