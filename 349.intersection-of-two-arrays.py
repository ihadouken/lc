class Solution:
    # Approach: Hashset, Complexity: O(m+n), O(min(m, n))
    # Tip: Throw the smaller array into a hashset. Then lookup every element of
    #      larger array in constant time. If there is a match, add to the set
    #      of common elements.

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums_small, nums_big = nums1, nums2
        else:
            nums_small, nums_big = nums2, nums1

        common = set()
        nums_small = set(nums_small)

        for num in nums_big:
            if num in nums_small:
                common.add(num)
        return common

    # Approach: Sorting + Binary Search, Complexity: O((m+n) * log(min(m, n))), O(1)
    # Note: Assume sorting and storing the output take up constant space.

    # Tip: Sort the smaller of the input arrays. Then iterate over the larger
    #      array and find every element of larger array in smaller array via
    #      binary search.

    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     if len(nums1) < len(nums2):
    #         nums_small, nums_big = nums1, nums2
    #     else:
    #         nums_small, nums_big = nums2, nums1
    #
    #     nums_small.sort()
    #     common = set()
    #
    #     for num in nums_big:
    #         if (self.bsearch(nums_small, num)):
    #             common.add(num)
    #     return common
    #
    # def bsearch(self, nums, target):
    #     l = 0
    #     r = len(nums) - 1
    #
    #     while l <= r:
    #         m = l + (r-l) // 2
    #         if nums[m] > target:
    #             r = m - 1
    #         elif nums[m] < target:
    #             l = m + 1
    #         else:
    #             return True
    #     return False
