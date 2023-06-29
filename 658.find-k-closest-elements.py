from math import floor
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        if size <= 1:
            return arr

        l = 0
        r = size - 1

        while l+1 < r:
            m = floor(l + (r-l) / 2)
            if arr[m] <= x:
                l = m
            else:
                r = m

        while k > 0:
            if r >= size or (l >= 0 and x - arr[l] <= arr[r] - x):
                l -= 1
            else:
                r += 1
            k -= 1
        # Return all elements in range (l, r)
        # i.e elements between l and r (non-inclusive).
        return arr[l+1:r]
