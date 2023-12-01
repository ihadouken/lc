# Approach: Min Heap
# Tip: Maintain a minheap of k largest elements. Root of heap = kth largest num.

class KthLargest:
    # Complexity: O((n-k)*logk) where n = size of nums. The heap can have k
    # elements max and the pop operation has to be performed n-k times.
    def __init__(self, k: int, nums: List[int]):
        # Use python list as heap.
        self.heap = []
        self.k = k

        # Initialize the k-length minheap using elements of nums.
        for num in nums:
            self.add(num)

    # Complexity: O(logk).
    def add(self, val: int) -> int:
        # Push the given element onto the heap.
        heapq.heappush(self.heap, val)

        # If the length of heap exceeds k, pop an element out of it.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Root of heap = current kth largest element.
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
