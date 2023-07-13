class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        merged = []

        # Try building result from both strings alternately. Check everytime
        # before adding from a string if has been exhausted. When both are
        # exhausted, we are done.
        while i < len(word1) or j < len(word2):
            merged.append(word1[i] if i < len(word1) else '')
            i += 1
            merged.append(word2[j] if j < len(word2) else '')
            j += 1

        return ''.join(merged)
