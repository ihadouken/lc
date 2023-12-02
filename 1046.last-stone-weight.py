class Solution:
    # Approach: Heap, Complexity: O(nlogn), O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Store all weights in a heap.
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        # Do a collision if 2 or more stones remain.
        while len(stones) > 1:
            # Take out two heaviest weights from heap.
            max_weight = heapq.heappop(stones)
            max_weight2 = heapq.heappop(stones)

            # Add weight of stone after collision and push it back onto the heap.
            new_weight = max_weight - max_weight2
            heapq.heappush(stones, new_weight)

        # Return 0 if no stones are left.
        if not stones:
            return 0
        # Otherwise return weight of last stone.
        return -stones[0]
