class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # first get the counts of each character in s1
        # then go through s2 using two pointers method iterating on the right pointer
        # if the count of the right character we add is too much subtract the left pointer
        #until the count becomes correct
        #if it's too little, move the right pointer forward
        #if we ever get a match return true
        #if the letter isn't in s1 reset everything and continue
        if len(s1) > len(s2): 
            return False

        l = 0 
        counts = {}
        for i in s1: 
            counts[i] = 1 + counts.get(i,0)

        for r in range(len(s2)): 
            c = s2[r]
            if c not in counts.keys(): 
                counts = {}
                for i in s1: 
                    counts[i] = 1 + counts.get(i,0)
                l = r + 1
                continue
            while counts[c] == 0: 
                counts[s2[l]] += 1
                l += 1
            counts[c] -= 1
            if (r - l + 1) == len(s1): 
                return True

        return False
