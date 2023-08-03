# Approach: Hashset, Complexity: O(n), O(n)
class Solution:
    def countDuplicated(self, nums: List[int]):
        """Calculate the number of elements in array that have a duplicate."""
        seen = set()
        duplicated = set()

        for num in nums:
            # Increment count only if the duplicacy of an element has just been found.
            if num in seen and num not in duplicated:
                duplicated.add(num)
            seen.add(num)

        return len(duplicated)

    def findPairs(self, nums: List[int], k: int) -> int:
        # k = 0 is a special case. In this case, we need the number of elements
        # in the array whose frequency exceeds one.
        if k == 0:
            return self.countDuplicated(nums)

        # Throw all elements into a hashset for quicker searching in an unsorted
        # array.
        uniques = set(nums)
        pair_count = 0

        # Find all numbers y such that y-k exists in hashset i.e. there exists
        # a pair (x, y) for which |x-y| = k.
        for num in uniques:
            if num-k in uniques:
                pair_count += 1

        return pair_count
