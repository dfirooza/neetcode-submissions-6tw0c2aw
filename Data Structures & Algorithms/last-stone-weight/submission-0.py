class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1: 
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            if first != second: 
                difference = abs(first - second)
                heapq.heappush(maxHeap, -difference)
        return abs(maxHeap[0]) if maxHeap else 0
        



        