class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []
        res = [-1] * N

        # Double pass to take care of circular aspect of array.
        for i in range(2*N):
            # Ensure index remains in range of nums.
            i %= N

            # Use monotonic (decreasing) stack to detect next greater element.
            # Store indices as they are required to write next greater for an
            # element in "res".
            while stack and nums[stack[-1]] < nums[i]:
                # If element > top is found, it is the top's next greater.
                idx = stack.pop()
                if res[idx] == -1:
                    res[idx] = nums[i]

                # Loop keeps on going to find more elements beneath top for which
                # current element next greater.

            # After processing stack items for which current element is next
            # greater, append the current element so that its next greater can
            # also be computed.
            stack.append(i)

        # Return array of corresponding next greater for each element in nums.
        return res
