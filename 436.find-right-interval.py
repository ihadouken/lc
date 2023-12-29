class Solution:
    # Approach: Sorting + Binary Search, Complexity: O(nlogn), O(1)
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Bsearch to find first (index minimization) interval S.T. start >= target.
        def bsearch(l, r, target):
            while l < r:
                m = l + (r - l) // 2
                if intervals[m][0] >= target:
                    r = m
                else:
                    l = m + 1

            if intervals[l][0] >= target:
                return l
            return -1

        # Store indices of interval for future lookup after sorting.
        for i, interval in enumerate(intervals):
            interval.append(i)

        N = len(intervals)
        res = [-1] * N
        intervals.sort()

        for i in range(0, N):
            # Binary search "right" for each interval[i] in range [i, N-1]. An
            # interval can be its own "right".
            right_idx = bsearch(i, N-1, intervals[i][1])

            # If a "right" is found, store its original index in res at original
            # index of interval[i].
            if right_idx != -1:
                res[intervals[i][2]] = intervals[right_idx][2]

        return res
