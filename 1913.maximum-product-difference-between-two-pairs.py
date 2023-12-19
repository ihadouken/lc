class Solution:
    # Approach: Greedy, Complexity: O(n), O(1)
    # Tip: To maximize w*x - y*z, maximize w*x and minimize y*z. To maximize w*z,
    #      maximize both w and x and to minimize y*z, minimize both y and z.

    def maxProductDifference(self, nums: List[int]) -> int:
        # Set appropriate defaults for maximums and minimums.
        max1 = max2 = 0
        min1 = min2 = float('inf')

        # Iterate over nums.
        for num in nums:
            # Update max1 or max2 according to element's value. Used "else if"
            # as values at distinct indices are to be selected.
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            # Update min1 or min2 according to element's value. A max and min
            # can have same value (index) as a potential min can't be ignored if
            # its momentarily set to max.
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        # Return the maximum product difference.
        return max1 * max2 - min1 * min2
