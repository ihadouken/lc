class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i, num in enumerate(nums):
            nums[i] = num * num;

        squares = []
        l = 0
        r = size - 1

        while l <= r:
            if nums[l] > nums[r]:
                squares.append(nums[l])
                l += 1
            else:
                squares.append(nums[r])
                r -= 1

        squares.reverse()
        return squares
