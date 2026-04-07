class Solution:
    def isValid(self, s: str) -> bool:
        types = {'(':')', '{':'}','[':']'}
        queue = []
        for i in s: 
            if i in types.values(): 
                if queue and i == queue[-1]: 
                    queue.remove(queue[-1])
                    continue 
                else: 
                    return False
            elif i in types.keys(): 
                queue.append(types[i])
        return len(queue) == 0


        