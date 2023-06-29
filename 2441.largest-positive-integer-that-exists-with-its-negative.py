class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = -1
        seen = set()

        for num in nums:
            if -num in seen:
                k = max(k, abs(num))
            seen.add(num)
        return k

