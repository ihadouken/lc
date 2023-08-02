class Solution:
    # Approach: Hashmap, Complexity: O(n), O(n)
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        freqs = {}

        # Record frequency of each element.
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        # Pairs possible for x = number of occurences of x+k.
        for num in nums:
            count += freqs.get(num+k, 0)

        # Return possible pairs in total.
        return count
