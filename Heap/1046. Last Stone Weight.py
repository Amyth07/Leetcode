import heapq
#Time -> O(n + nlogn)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -abs(x-y))

        return 0 if not heap else -heap[0]
            
            
            