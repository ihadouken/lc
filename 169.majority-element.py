class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach HashMap, Complexity: O(n), O(n)
        freqs = {}
        # Record frequencies of elements.
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        # Find (n/2)+1 among frequencies and return its corresponding element.
        for num, freq in freqs.items():
            if freq >= len(nums)//2 + 1:
                return num

        # Approach: Sorting, Complexity: O(nlogn), O(1)
        # When sorted, index n/2 always has an instance of majority.
        # nums.sort()
        # return nums[len(nums)//2]
