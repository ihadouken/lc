class Solution:
    # Approach: Hashset, Complexity: O(n), O(n)
    # Tip: For nums to be broken into equal pairs, every element entering set
    #      must also leave it and set must be empty after processing nums.

    def divideArray(self, nums: List[int]) -> bool:
        toggle = set()

        for num in nums:
            if num not in toggle:
                toggle.add(num)
            else:
                toggle.remove(num)

        return len(toggle) == 0
