class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for f in freq.values():
            if f == 1:
                return -1
            ops += math.ceil(f/3)

        return ops
