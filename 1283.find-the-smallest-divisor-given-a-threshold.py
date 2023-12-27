class Solution:
    # Approach: Binary Search, Complexity: O(n * max(nums)), O(1)
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Find sum of quotients when array elements are divided by given divisor.
        def findSum(div: int) -> int:
            sum = 0
            for num in nums:
                sum += math.ceil(num/div)
            return sum

        # Unity is smallest valid divisor. Upper bound for divisor is max(nums)
        # as it is the smallest divisor which produces 1 for each element.
        l, r = 1, max(nums)

        # Binary Search to minimize d such that findSum(d) <= threshold.
        while l < r:
            m = l + (r-l) // 2
            sum = findSum(m)

            if sum > threshold:
                l = m + 1
            else:
                r = m

        return l
