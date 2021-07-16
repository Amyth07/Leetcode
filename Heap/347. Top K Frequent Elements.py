import collections
import heapq

# Time -> O(n + klogN)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = res = []

        for key, freq in counter.items():
            # heapq uses first ele of tuple for building heap, hear using neg to treat min heap ad max heap
            heapq.heappush(heap, (-freq, key))
        
        print(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
