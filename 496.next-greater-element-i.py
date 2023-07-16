class Solution:
    # # Approach: Hashmap + Linear Search, Complexity: O(m*n), O(n)
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # Prepopulate res to avoid "index out of range".
    #     res = [0] * len(nums1)
    #     # Store nums1 in a hashmap. This helps us to check if element of nums2
    #     # exists in nums1 and get its index (to store next greater in res) in
    #     # O(1) time.
    #     num1map = {num:i for i, num in enumerate(nums1)}
    #
    #     for i, num in enumerate(nums2):
    #         # Find next greater only if number exists in nums1.
    #         if num in num1map:
    #             j = i + 1
    #             # O(n)
    #             while j < len(nums2) and nums2[j] <= num:
    #                 j += 1
    #
    #             # If no greater is found to the right use -1.
    #             greater = -1 if j == len(nums2) else nums2[j]
    #             # Find the index of num in nums1. Then put it in corresponding
    #             # index in res.
    #             res[num1map[num]] = greater
    #     return res

    # Approach: Hashmap + Monotonic Stack, Complexity: O(m+n), O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        num1map = {num:i for i, num in enumerate(nums1)}
        stack = []

        for num in nums2:
            # Check if num is "next greater" for top of the stack. num may be
            # the "next greater" for multiple values so keep checking the
            # condition for new tops after popping.
            while stack and num > stack[-1]:
                popped = stack.pop()
                res[num1map[popped]] = num

            # Store in stack only if we need to find "next greater" for num.
            if num in num1map:
                stack.append(num)
        return res
