class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #given: an array of CPU tasks "tasks", and an integer n 
        #return: the min number of CPU cycles required to complete all tasks    

        #solution: use a max heap, initially iterate through tasks and push (0,task)
        #on each turn push the max value and add 1 to the num cycles and pop that and add it back with value 0
        #if the max is less than n then just idle and add 1 to cycles and continue
        
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)
        time = 0
        q = deque()

        while heap or q: 
            time += 1
            if heap: 
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time: 
                heapq.heappush(heap, q.popleft()[0])
        
        return time
        





        