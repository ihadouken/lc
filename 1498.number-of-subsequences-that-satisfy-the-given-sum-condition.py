class Solution:
    # Approach: Sorting + Two Pointer, Complexity: O(nlogn), O(1)
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Sort the input so that values are conveniently increasing left to right
        # but decreasing right to left.
        nums.sort()
        res = 0

        # Two pointers converge towards one another from extreme ends.
        l = 0
        r = len(nums) - 1

        # If r > l, no valid subsequence is possible.
        while l <= r:
            # If min (left) + max (right) exceeds target, max must be decreased.
            if nums[l] + nums[r] > target:
                r -= 1

            # If the sum is <= target, record number of all subsequences strictly
            # starting from min (left) i.e. 2^(r-l). 2^(r-l) instead of 2^(r-l+1)
            # as min (one of the element) is fixed in the subseq. Min Fixing is
            # reqd. as subseq may assume a higher min by excluding current min
            # for which min + max <= t may not be valid.
            else:
                res += 1 << r-l
                # Now, try subsequences with a higher mins until the condition
                # again stops holding true and max has to be decreased.
                l += 1

        # Mod by a large prime as no. of valid subsequences may be large.
        return res % 1000000007
