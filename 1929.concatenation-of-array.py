class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # for i in range(2*len(nums)):
        #     ans.append(nums[i % len(nums)])

        for _ in range(2):
            for num in nums:
                ans.append(num)
        return ans
