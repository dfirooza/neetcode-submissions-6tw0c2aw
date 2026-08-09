class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #given: an array nums of unique integers
        #return: all the possible permutations
        #do a for loop where each time at the beginning you popleft from the current list, and at the end append to it
        #in the middle of it dfs on the rest of the list after you pop

        res = []
        option = deque(nums)

        def dfs(option, here): 
            if not option: 
                res.append(here[:])
                return
            for _ in range(len(option)):
                current = option.popleft()
                here.append(current)
                dfs(option, here)
                here.pop()
                option.append(current)
            
        dfs(option, [])
        return res