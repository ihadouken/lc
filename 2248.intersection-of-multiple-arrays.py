class Solution:
    # Approach: Counting, Complexity: O(n+k), O(k)
    # where n -> total number of elements,
    #       k -> 1000.

    # Tip: Store count of each number (at index = number) in an array. For number
    #      to be in the intersection, it has to occur in every array. Thus, count
    #      must equal the number of arrays in nums.

    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = [0] * 1001
        res = []

        for array in nums:
            for num in array:
                counts[num] += 1

        for i, count in enumerate(counts):
            if count == len(nums):
                res.append(i)

        return res

    # Approach: Counting + Hashmap + Sorting, Complexity: O(n + ilogi), O(n)
    # where n -> total number of elements,
    #       i -> number of elements in intersection.

    # def intersection(self, nums: List[List[int]]) -> List[int]:
    #     counts = {}
    #
    #     for array in nums:
    #         for num in array:
    #             counts[num] = counts.get(num, 0) + 1
    #
    #     res = [num for num, count in counts.items() if count == len(nums)]
    #     res.sort()
    #     return res
