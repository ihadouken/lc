class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i, digit in reversed(list(enumerate(digits))):
            if digit != 9:
                break
            digits[i] = 0
        else:
            digits.insert(0, 1)
            return digits

        digits[i] += 1
        return digits
