class Solution:
    # Approach: Sliding Window, Complexity: O(n), O(1)
    # Tip: abs(i-j) <= k means check all windows of size k+1 because the array
    #      indices are 0-based i.e. r-l+1 <= k+1 or r-l <= k.

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Store the window in a hashset for quick query for a element.
        win = set()
        l = 0

        # Check all windows of size k+1 using sliding window technique.
        for r, num in enumerate(nums):
            # If window size is at its limit remove an existing element i.e.
            # oldest element in the window. This element is always the left
            # end of the window.
            if r - l > k:
                win.remove(nums[l])
                l += 1

            # If num already exits in the window, the current element is its duplicate.
            if num in win:
                return True
            # Else add the element to the window.
            win.add(num)

        # There was no duplicate in any window.
        return False

