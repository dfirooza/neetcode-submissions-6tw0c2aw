class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we need to find the k points which minimized the euclidean distance equation
        #first let's map each point to its corresponding euclidean distance, distance should be the key
        #then we'll make a list of just distances 
        #then we'll heapify this list into a max heap, and we'll pop from it k times, each time ew use the 
        #map to finding the corresponding point and appending that to our output list

        heap = []
        for point in points: 
            value = point[0]**2 + (point[1])**2
            heap.append((value, point))
        heapq.heapify(heap)
        output = []
        for _ in range(k): 
            dist, point = heapq.heappop(heap)
            output.append(point)
        return output

        
            
        
        
        