# Approach: Hashset, Complexity: O(n), O(n)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min1, min2, maxval = arr[0], arr[1], max(arr)

        # Find the min and 2nd min element.
        for num in arr:
            if num < min1:
                min2 = min1
                min1 = num
            elif num != min1 and num < min2:
                min2 = num

        # Edge case: A.P. with common diff = 0.
        if (min1 == maxval):
            return True

        # Find common diff using min and 2nd min.
        cdiff, element, seen = min2 - min1, min1, set()

        # Build set out of the array for O(1) lookup.
        for num in arr:
            # Duplicates can't be accomodated in A.P. if common diff != 0.
            if num in seen:
                return False
            seen.add(num)

        # Check if all A.P. elements for their presence.
        while element <= maxval:
            if element not in seen:
                return False

            # Remove every acknowledged element.
            seen.remove(element)
            element += cdiff

        # If all array elements constite an A.P., entire set if used up.
        return not seen
