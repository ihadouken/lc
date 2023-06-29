class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chcounts = {}
        for ch in s:
            if ch not in chcounts:
                chcounts[ch] = 0
            chcounts[ch] += 1

        for ch in t:
            if ch not in chcounts:
                return False
            chcounts[ch] -= 1

        for count in chcounts.values():
            if count:
                return False

        return True
