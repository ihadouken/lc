class Solution:
    # Approach: Sliding Window + Hashmap, Complexity: O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Trivial case with no window possible.
        if not s:
            return 0

        # Initialize window with first element.
        seen = {s[0]}
        l = 0
        res = 1

        for r, ch in enumerate(s):
            if ch in seen:
                # Pop elements from the window until the duplicate is found.
                while l < r and s[l] != ch:
                    seen.remove(s[l])
                    l += 1
                # Remove the duplicate. Its later occurence is in the window
                # so no need to remove it from the set.
                if l != r:
                    l += 1
            else:
                # Add unique element to window and check if the current
                # substring is longer than the previous longest.
                seen.add(ch)
                res = max(res, r-l+1)
        return res
