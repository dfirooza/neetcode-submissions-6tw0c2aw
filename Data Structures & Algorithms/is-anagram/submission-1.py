class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {} 
        if len(s) != len(t): 
            return False
        for i in s: 
            seen[i] = seen.get(i, 0) + 1
        for i in t: 
            if i not in seen: 
                return False 
            else:
                if seen[i] == 0: 
                    return False 
                else: 
                    seen[i] -= 1
        return True


        