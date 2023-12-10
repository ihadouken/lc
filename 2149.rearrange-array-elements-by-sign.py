class Solution:
    # Complexity: O(n), O(n)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        # Throw -ve and +ve elements (in order) in auxillary arrays.
        part1 = [num for num in nums if num < 0]
        part2 = [num for num in nums if num >= 0]

        # Build the result by adding one +ve and then one -ve.
        for neg, pos in zip(part1, part2):
            res.extend([pos, neg])

        return res
