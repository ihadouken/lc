class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rear, front = 0, -1
        q = collections.deque()
        res = []
        l = 0

        for r, num in enumerate(nums):
            while q and nums[q[front]] <= nums[r]:
                q.pop()
            q.append(r)

            if r-l+1 == k:
                res.append(nums[q[rear]])

                if q[rear] == l:
                    q.popleft()
                l += 1

        return res
