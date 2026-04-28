class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # to do this we must find the total cost of each path
        # and then return the minimum of these costs
        # so we must first compute each path using dfs
        # however paths are repeated, we can find the leftmost path then 
        # based on that for the right ones just use the single path 
        prev, curr = 0, 0
        for i in range(2, len(cost) + 1): 
            prev, curr = curr, min(curr + cost[i-1], prev + cost[i-2])
        return curr        