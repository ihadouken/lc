class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # suffix = 1
        # for num in reversed(nums):
        #     res.append(suffix)
        #     suffix *= num
        # res.reverse()
        #
        # prefix = 1
        # for i, num in enumerate(nums):
        #     res[i] *= prefix
        #     prefix *= num

        res = []
        prefix = 1
        for num in nums:
            res.append(prefix)
            prefix *= num

        suffix = 1
        for i, num in reversed(list(enumerate(nums))):
            res[i] *= suffix
            suffix *= num

        return res
