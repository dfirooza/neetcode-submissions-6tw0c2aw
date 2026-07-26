class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #given an integer array and a integer h
        #must decide the min k to finish eating bananas in h hours
        bot = 1
        top = max(piles)

        while bot <= top: 
            mid = bot + (top - bot)//2
            hours = sum(math.ceil(pile/mid) for pile in piles)
            if hours <= h: 
                top = mid - 1
            else: 
                bot = mid + 1
        return bot
        

