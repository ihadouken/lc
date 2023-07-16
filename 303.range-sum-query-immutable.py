# Approach: Prefix Sum, Complexity: O(1) for each query.
class NumArray:
    # Create prefix sum array from the input array.
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        sum = 0

        for num in nums:
            sum += num
            self.prefix.append(sum)

    # prefix[x] means the sum of all elements upto index x. Thus, sumRange(x, y)
    # can be calculated by subtracting the sum of all elements upto index x-1
    # i.e. prefix[x] from the sum of all elements upto index y i.e. prefix[y+1].
    # prefix[0] means the sum of no elements and thus always equals to 0. It is
    # present to account for cases like sumRange(x, 0) where we need to subtract
    # zero from prefix[x+1].
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
