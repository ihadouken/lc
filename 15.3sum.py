class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        i = 0

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            target = -nums[i]
            j, k = i + 1, len(nums) - 1

            while (j < k):
                sum = nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while (nums[j] == nums[j-1] and j < k):
                        j += 1

        return triplets
