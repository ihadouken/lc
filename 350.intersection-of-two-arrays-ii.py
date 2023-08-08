class Solution:
    # Approach: Hashmap, Complexity: O(m+n), O(min(m, n))
    # Tip: Record the elements of the smaller array along with their frequencies
    #      in a hashmap. Iterate over the other array. If a match is found in
    #      the hashmap, decrement its count. This is because one instance of the
    #      element in the smaller array has been exhausted i.e. an element common
    #      with it has been found in other array.

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums_small, nums_big = nums1, nums2
        else:
            nums_small, nums_big = nums2, nums1

        nums_small_freq = {}
        for num in nums_small:
            nums_small_freq[num] = nums_small_freq.get(num, 0) + 1

        common = []
        nums_small = set(nums_small)

        for num in nums_big:
            if num in nums_small_freq:
                common.append(num)
                if nums_small_freq[num] == 1:
                    nums_small_freq.pop(num)
                else:
                    nums_small_freq[num] -= 1
        return common
