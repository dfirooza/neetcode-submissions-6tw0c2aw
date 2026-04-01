class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        initial = {}
        for index, x in enumerate(nums): 
            need = target - x
            if need in initial: 
                return [initial[need], index]
            initial[x] = index
            
        



                
