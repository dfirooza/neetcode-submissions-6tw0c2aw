class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """heapq.heapify_max(nums)
        for i in range(1,k): 
            heapq.heappop_max(nums)
        max = heapq.heappop_max(nums)
        return max"""
        heap = []
        for num in nums: 
            heapq.heappush(heap, num)
            if len(heap) > k: 
                heapq.heappop(heap)
        return heap[0]
        