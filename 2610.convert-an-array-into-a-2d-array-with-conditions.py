class Solution:
    # Approach: Hashmap, Complexity: O(n), O(n)
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqs = {}
        rows = []

        # Use hashmap to store frequencies of each number.
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        # Continue creating rows until occurences of all numbers run out.
        while freqs:
            # Hashmap's keys is a list unique elements with at least 1 instance
            # ununsed. Use all elements available in a row to minimize rows.
            rows.append(list(freqs.keys()))

            # Decrement each key and remove keys (numbers) with 0 instances left.
            # Iterate over backup list of keys as python doesn't allow modifying
            # hashmap while iterating over them.
            for num in list(freqs.keys()):
                if freqs[num] == 1:
                    freqs.pop(num)
                else:
                    freqs[num] -= 1

        # Return list of all generated rows.
        return rows
