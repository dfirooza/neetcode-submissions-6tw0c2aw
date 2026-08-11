class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #given: an integer array coins representing coins of different denominations and an integer amount 
        #representing a target amount of money
        #return: the feweest number of coins that you need to make up the exact target amount 
        #solution: at each step you can choose anywhere from zero to amount//curr of the coin 
        #actual solution: at each step the result is the solution to whether the current + recursion on the rest 
        #would work

        dp = [amount + 1] * (amount+1)
        dp[0] = 0 

        for i in range(1, amount + 1): 
            for j in coins: 
                if i - j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-j])
        return dp[amount] if dp[amount] != amount + 1 else -1
