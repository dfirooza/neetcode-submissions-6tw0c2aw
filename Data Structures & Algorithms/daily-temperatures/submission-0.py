class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures): 
            while stack and stack[-1][0] < t: 
                curr_t, curr_i = stack.pop()
                res[curr_i] = i - curr_i
            stack.append([t, i])
        return res

            
            