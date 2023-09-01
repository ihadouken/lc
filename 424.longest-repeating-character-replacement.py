class Solution:
    # Appraoch: Sliding Window + Hashmap, Complexity: O(n*26), O(26)
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        l, winsize, res = 0, 0, 0

        for r, ch in enumerate(s):
            # Add the current char to the window.
            freqs[ch] = freqs.get(ch, 0) + 1
            winsize += 1

            # Optimal replacement involves finding the most frequent char and
            # replacing all other char with it so that number of replacements
            # in minimum. If the number of chars other than the most frequent
            # is higher than k, the current window is invalid. Make it valid
            # again by shrinking it from the left.
            while l < r and winsize - max(freqs.values()) > k:
                freqs[s[l]] -= 1
                l += 1
                winsize -= 1

            # Keep track of length of most optimal (largest valid) window.
            res = max(res, winsize)

        # Return size of most optimal window.
        return res
