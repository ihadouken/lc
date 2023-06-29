class Solution:
    def binstr2dec(self, binstr: str) -> int:
        dec = 0
        for bit in binstr:
            dec = dec * 2 + int(bit)
        return dec

    def addBinary(self, a: str, b: str) -> str:
        if a == '0': return b
        if b == '0': return a

        sum = self.binstr2dec(a) + self.binstr2dec(b)
        result = []
        while sum > 0:
            result.append(str(sum%2))
            sum //= 2
        return (''.join(reversed(result)))
