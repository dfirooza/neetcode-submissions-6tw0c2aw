class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #given: an integer array
        #return: max amount of water a container can store
        #at each step, if moving the left pointer by one gives a better total do that
        #if it doesn't then try moving the right pointer back by one
        #if neither work just move left forward by one
        #if it's already beating the max, just move on and let the next loop do its thing
        l = 0 
        r = len(heights) - 1
        maximum = 0
        while l < r: 
            curr = min(heights[l], heights[r]) * (r-l)
            maximum = max(maximum, curr)
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1
        return maximum

        
        
        