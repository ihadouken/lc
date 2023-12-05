class Solution:
    # Approach: Sorting + Two Pointer, Complexity: O(n), O(n)
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Sort the input so that 
        nums.sort()

        MOD = 1000000007
        res = 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 1 << r-l
                l += 1

        return res % MOD
