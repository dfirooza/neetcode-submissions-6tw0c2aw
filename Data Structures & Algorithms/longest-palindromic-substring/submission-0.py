class Solution:
    def longestPalindrome(self, s: str) -> str:
        #given: a string s
        #return the longest substring of s that is a palindrome
        #this is dp because in each step you should break it into smaller problems 
        #of the longest palindromic substring for a specific substring within the input string s 
        #use two pointers
        #two cases, one case is where the beginning and end pointer are equal, here just return longestPalindrome
        #in the case they're not equal
        resLen = 0 
        res = ""

        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > resLen: 
                    resLen = r-l+1
                    res = s[l:r+1]
                l-= 1
                r += 1
            l, r = i, i + 1
            while l>=0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > resLen: 
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
    
            


