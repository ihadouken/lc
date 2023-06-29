class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num > 0:
                seen.add(num)

        for positive in range(1, len(nums)+1):
            if positive not in seen:
                return positive
        return len(nums) + 1
