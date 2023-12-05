class Solution:
    # Approach: Maxheap, Complexity: O(nlogk), O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Maxheap easily evicts the farthest point when heap has > k points.
        maxheap = []

        # Iterate over all given points.
        for x, y in points:
            # Add the point along with computed distance from origin to heap.
            d = x*x + y*y
            heapq.heappush(maxheap, (-d, x, y))

            # When heap has an extra point, evict the farthest point.
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        # Build the result from the final points in maxheap.
        return [[x, y] for _, x, y in maxheap]
