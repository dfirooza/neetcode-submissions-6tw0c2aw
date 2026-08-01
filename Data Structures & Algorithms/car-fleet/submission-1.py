class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #given: two arrays of integers position and speed, both length n 
        #return: the number of diff car fleets that will arrive at the destination
        #to determine where each car will end up 
        #first calculate the target - the current position of that car
        #calculate how long it will take that car to catch up to the next 
        #calculate how long it will take that car to reach the destination
        #take the min of those two, if it catches up first consider it in the fleet of the next car
        #the time complexity suggests tahat there's some kind of binary search going on 

        
        maps = {}
        for index, val in enumerate(position): 
            maps[val] = ((target-val)/speed[index])
        
        position.sort()
        total = 1
        maximum_time = maps[position[-1]]
        for val in reversed(position): 
            curr = maps[val]
            if curr <= maximum_time: 
                continue
            else: 
                maximum_time = curr
                total += 1
        return total


        

        #we now have a mapping from each index to it's distance to target and it's speed


        
            
        
        
        