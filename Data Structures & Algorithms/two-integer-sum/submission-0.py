class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        initial = {}
        for index, i in enumerate(nums): 
            initial[i] = index
        for index, i in enumerate(nums): 
            need = target - i
            if need in initial.keys(): 
                if index != initial[need]: 
                    return [index, initial[need]]
        



                
