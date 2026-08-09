class Solution:
    def countSubstrings(self, s: str) -> int:
        #given: a string s 
        #return: the number of substrings within s that are palindromes
        #solution: go through once, expand from each letter and each time the first and last letter match a palindrome
        count = 0
        for i in range(len(s)): 
            l, r = i, i
            while l >=0 and r < len(s) and s[l]==s[r]: 
                count += 1
                l-=1 
                r+= 1
        
        for i in range(len(s)): 
            l, r = i, i + 1
            while l >=0 and r < len(s) and s[l]==s[r]: 
                count += 1
                l-=1 
                r+= 1
        return count