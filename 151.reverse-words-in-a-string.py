class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        s = s.strip()
        beg = len(s) - 1
        for forward, ch in reversed(list(enumerate(s))):
            if ch == " ":
                if beg == forward:
                    beg -= 1
                else:
                    ans += s[forward+1:beg+1] + " "
                    beg = forward - 1
        ans += s[forward:beg+1]
        return ans
