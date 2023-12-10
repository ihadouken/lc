class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # res = []
        # for num in nums:
        #     if num < pivot:
        #         res.append(num)
        #
        # for num in nums:
        #     if num == pivot:
        #         res.append(pivot)
        #
        # for num in nums:
        #     if num > pivot:
        #         res.append(num)
        #
        # return res

        smaller = [num for num in nums if num < pivot]
        larger = [num for num in nums if num > pivot]

        pivots = nums.count(pivot)
        for _ in range(pivots):
            smaller.append(pivot)

        smaller.extend(larger)
        return smaller
