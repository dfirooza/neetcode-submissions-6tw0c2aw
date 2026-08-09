class Solution:
    def numDecodings(self, s: str) -> int:
        #given: a string of uppercase english characters
        #return: the number of ways to decode the message 
        #use dp by at each step adding the 1 + the number of ways to map 
        #at each step you can either attach the number or separate it
        #count the number of ways the first number can be arranged and add that to numDecodings of the rest  
        dp = {len(s): 1}   
        def dfs(i):  
            if i in dp: 
                return dp[i]
            if s[i] == "0": 
                return 0
            res = dfs(i+1)
            if (i+1<len(s) and (10<= int(s[i:i+2]) <= 26)): 
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)
