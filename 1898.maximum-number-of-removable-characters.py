class Solution:
    # Return a copy of string with all marked ('0') chars removed.
    def deleteChars(self, s: str, removable: List[int], until: int) -> str:
        s = list(s)
        i = 0

        while i <= until:
            s[removable[i]] = '0'
            i += 1

        return ''.join(s)

    # Check if p is subsequence of s.
    def isSubsequence(self, s: List[str], p: str) -> bool:
        i = j = 0

        while (i < len(s) and j < len(p)):
            if p[j] == s[i]:
                j += 1
            i += 1

        return j == len(p)

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        k = 0
        l = 0
        r = len(removable) - 1

        # Run a binary search over "removable" and maximize k such that after
        # deleting chars at indices specified from removable[0] to removable[k-1]
        # in s, p is still a subsequence of s.
        while l <= r:
            m = l + (r-l) // 2;
            newstr = self.deleteChars(s, removable, m)

            if self.isSubsequence(newstr, p):
                k = m + 1
                l = m + 1
            else:
                r = m - 1

        return k
