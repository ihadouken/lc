class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def findSum(threshold):
            sum = 0

            for num in arr:
                # Limit all numbers > threshold to threshold.
                if num > threshold:
                    sum += threshold
                # Other numbers are considered as-is.
                else:
                    sum += num

            # Return sum of mutated array after limitation.
            return sum

        # Lower bound must produce maximum decrease in array sum. 0 is used as
        # every element > 0 and hence every element is limited to 0 and sum = 0.
        # Upper bound must produce no decrease in array sum. Max element is used
        # as no element > max and hence no elements are limited.
        l, r = 0, max(arr)

        # Binary search to minimize threshold that produces sum closest to target.
        while l + 1 < r:
            m = l + (r - l) // 2
            sum = findSum(m)

            if sum >= target:
                r = m
            else:
                l = m

        # Post processing for optimal result from last two nums in search space.
        if abs(target-findSum(l)) <= abs(target-findSum(r)):
            return l
        return r
