class Solution:
    # Approach: Binary Search + Two Pointer, Complexity: O(n * log(max(matrix)-min(matrix))), O(1)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessOrEqual(pivot: int) -> int:
            count = 0
            j = N-1

            # Start at top-right and descend one row at a time.
            for row in matrix:
                # Move left until element <= pivot is found in row.
                while j >= 0 and row[j] > pivot:
                    j -= 1
                # All elements in range [0, j] <= pivot as each row is sorted.
                count += j + 1

                # There is no need to check indices > j in next row because
                # A[i][j+1] > pivot and A[i+1][j+1] > A[i][j+1] due to columns
                # being sorted which implies A[i+1][j+1] > pivot.

            # Return grand total of elements <= pivot.
            return count

        # Lower Bound has 0 elements <= to itself i.e. min(matrix) which is found
        # at top-left corner. Upper bound has all (N^2 - 1) elements <= to itself
        # i.e. max(matrix) which is found at bottom-right corner.
        N = len(matrix)
        l, r = matrix[0][0], matrix[N-1][N-1]

        # Binary search to minimize element with at least k elements <= to itself.
        while l < r:
            m = l + (r - l) // 2
            if countLessOrEqual(m) >= k:
                r = m
            else:
                l = m + 1

        return l


    # Approach: N Pointers + Minheap + Greedy, Complexity: O((k+n) * logn), O(n)
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     # Maintain a pointer for smallest unprocessed element of each row.
    #     # Use a minheap to easily select the minimum out of all elements.
    #     N = len(matrix)
    #     minheap = [(row[0], i, 0) for i, row in enumerate(matrix)]
    #     heapq.heapify(minheap)
    #
    #     # Keep processing elements until the kth element is processed.
    #     while k:
    #         # Greedily select minimum element out of smallest unprocessed elements
    #         # of all rows and the next element in its row to heap as next
    #         # candidate to be processed.
    #         res, i, j = heapq.heappop(minheap)
    #         if j < N-1:
    #             heapq.heappush(minheap, (matrix[i][j+1], i, j+1))
    #
    #         # Update counter to decrease no. of elements required to be processed.
    #         k -= 1
    #
    #     # Return the kth element processed.
    #     return res

    # Approach: Maxheap, Complexity: O(n^2 * logk), O(k)
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     maxheap = []
    #
    #     for row in matrix:
    #         for num in row:
    #             heapq.heappush(maxheap, -num)
    #             if len(maxheap) > k:
    #                 heapq.heappop(maxheap)
    #
    #     return -maxheap[0]
