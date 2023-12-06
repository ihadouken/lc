class Solution:
    # Approach: Quickselect + Lomuto Partitioning, Complexity: O(n) (average), O(1)
    # Standard partitioning function using random pivots.
    def partition(self, arr: List[List[int]], beg: int, end: int):
        i = j = beg
        pivot = random.randint(beg, end)
        arr[pivot], arr[end] = arr[end], arr[pivot]

        while i < end:
            if arr[i][0] < arr[end][0]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
            i += 1

        arr[end], arr[j] = arr[j], arr[end]
        return j


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Precompute distance for each point. Square rooting is unnecessary.
        for i, (x, y) in enumerate(points):
            points[i] = (x*x + y*y, x, y)

        # Initialize beg and end as two extreme ends of input.
        beg, end = 0, len(points) - 1

        # Continue until subarray to be partitioned is valid.
        while beg < end:
            # Partition the subarray.
            p = self.partition(points, beg, end)

            # If partition contains less than k closest points, redo partitioning
            # for rest of points.
            if p < k:
                beg = p + 1;

            # If more than k closest points are selected, enrich the current
            # selection so it contains the k closest points.
            elif p > k:
                end = p - 1;

            # If exactly k points were selected, desired k points are found.
            else:
                break

        # Modify input to remove distances added earlier.
        for i, (_, x, y) in enumerate(points):
            points[i] = [x, y]

        # First k points in array are closest to origin.
        return points[:k]

    # # Approach: Maxheap, Complexity: O(nlogk), O(k)
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     # Maxheap easily evicts the farthest point when heap has > k points.
    #     maxheap = []
    #
    #     # Iterate over all given points.
    #     for x, y in points:
    #         # Add the point along with computed distance from origin to heap.
    #         d = x*x + y*y
    #         heapq.heappush(maxheap, (-d, x, y))
    #
    #         # When heap has an extra point, evict the farthest point.
    #         if len(maxheap) > k:
    #             heapq.heappop(maxheap)
    #
    #     # Build the result from the final points in maxheap.
    #     return [[x, y] for _, x, y in maxheap]
