class Solution:
    # Approach: Hashmap, Complexity: O(n), O(26)
    # Tip: To maximize length, keep track of only first (min index) occurence of
    #      every char. Iterate and maximize (index - first occurence index - 1).

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occ = {}
        maxlen = -1

        for i, ch in enumerate(s):
            if ch not in first_occ:
                first_occ[ch] = i
            else:
                maxlen = max(maxlen, i-first_occ[ch]-1)

        return maxlen
