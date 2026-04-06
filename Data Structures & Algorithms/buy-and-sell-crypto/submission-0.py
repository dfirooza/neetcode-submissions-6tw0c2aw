class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for index, val in enumerate(prices[:-1]): 
            curr_profit = max(prices[index+1:]) - val
            if curr_profit > maximum: 
                maximum = curr_profit
        return maximum        
            

            
        