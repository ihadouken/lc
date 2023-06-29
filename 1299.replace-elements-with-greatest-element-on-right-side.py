class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i, item in reversed(list(enumerate(arr))):
            arr[i] = max
            if item > max:
                max = item
        return arr
