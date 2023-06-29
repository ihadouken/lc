from math import floor


class Solution:
    def first_occurrence(self, nums: List[int], target: int) -> int:
        """Find minimum k such that nums[k] <= target."""
        l = 0
        r = len(nums) - 1

        while l+1 < r:
            m = floor(l + (r-l) / 2)
            if nums[m] >= target:
                r = m
            else:
                l = m

        if nums[l] == target:
            min = l
        elif nums[r] == target:
            min = r
        else:
            min = -1

        return min

    def last_occurrence(self, nums: List[int], target: int) -> int:
        """Find maximum k such that nums[k] >= target."""
        l = 0
        r = len(nums) - 1

        while l+1 < r:
            m = floor(l + (r-l) / 2)
            if nums[m] <= target:
                l = m
            else:
                r = m

        if nums[r] == target:
            max = r
        elif nums[l] == target:
            max = l
        else:
            max = -1

        return max

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [self.first_occurrence(nums, target), self.last_occurrence(nums, target)]
