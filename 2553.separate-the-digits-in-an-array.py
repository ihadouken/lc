class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            digits = []

            while num > 0:
                digits.append(num%10)
                num //= 10

            digits.reverse()
            res.extend(digits)

        return res
