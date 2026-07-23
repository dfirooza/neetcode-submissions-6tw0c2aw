class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        for i in range(1,k): 
            heapq.heappop_max(nums)
        max = heapq.heappop_max(nums)
        return max