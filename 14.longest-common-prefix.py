class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = []
        for col in zip(*strs):
            prev = col[0]
            for ch in col:
                if prev != ch:
                    return ''.join(lcp)
            lcp.append(ch)
        return ''.join(lcp)
