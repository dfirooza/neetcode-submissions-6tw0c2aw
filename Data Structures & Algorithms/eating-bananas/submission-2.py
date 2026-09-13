class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #given: an integer array where index represent number of bananas, an integer which represents number of hours to eat all 
        #the bananas 
        #return: the min integer k such that you can eat all the bananas within h hours 
        #solution: sort the array first

        #the max amount of time it can take is max(piles) hours 
        #ceil/k time is needed for each pile 

        left = 1 
        right = max(piles)

        while left <= right: 

            k = (left + right)//2
            hours = 0 

            for pile in piles: 
                hours += math.ceil(pile/k)

            if hours <= h: 
                right = k - 1
            
            else: 
                left = k + 1

        return left
        


        
        