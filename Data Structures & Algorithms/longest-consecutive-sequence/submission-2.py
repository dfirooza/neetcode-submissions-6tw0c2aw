class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #given: array of integers numbers
        #return: length of longest consecutive sequence of elements
        num_set = set(nums)
        max_len = 0 

        for val in num_set: 
            if val - 1 not in num_set: 
                length = 1
                while val + length in num_set: 
                    length += 1
                max_len = max(max_len, length)
        return max_len


        """
        freq = {}
        length = 1
        max_len = 0 

        for i in nums: 
            freq[i] = 1 + freq.get(i, 0)

        for index, val in enumerate(nums): 
            if freq.get(val-1, 0) > 0: 
                length += 1
                freq[val-1] -= 1
            else: 
                freq = {}
                for i in nums: 
                    freq[i] = 1 + freq.get(i,0)
                    length = 1
            max_len = max(max_len, length)
        return max_len"""
                
            


       

        