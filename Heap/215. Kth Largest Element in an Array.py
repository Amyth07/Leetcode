import heapq
# Time(N + klogN)

# Heap creation -> O(n)
# Heap poping an element -> O(logN)
# Heap inserting an element -> O(logN)
# Heap finding min/max -> O(1)
# Heapify -> O(NlogN)


# By default heapq uses min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            # Reverting the sign so that I can use this as max heap
            heapq.heappush(heap, -num)
        for _ in range(k-1):
            # This will always pop the smallest element.
            heapq.heappop(heap)
        return -heapq.heappop(heap)



# the same can be achieved by using the min heap, using the window of k elements, the last window will have the smallest element in k sized window.
# this is a min heap and since we are removing smallest node from the heap root each time the lenght exceeds k, at the end of the loop we'll be having the largest element at the root of the heap, just pop and return
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
