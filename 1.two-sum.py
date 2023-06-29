class Solution:
    def twoSum(self, nums, target):
        hash_table = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[num] = i
