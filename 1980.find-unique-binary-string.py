class Solution:
    # Procedure Complexity: O(n), O(1)
    def bin2dec(self, binary: str) -> int:
        decimal = 0

        for bit in binary:
            decimal = decimal * 2 + int(bit)

        return decimal

    # Approach: Bit Hacks + Hashset, Complexity: O(n^2), O(n)
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        N = len(nums)
        # Store decimals equivalent of binary strings in hashset.
        decimals = {self.bin2dec(num) for num in nums}

        # Find the first number not in hashset.
        for num in range(0, 1 << N):
            if num not in decimals:
                break

        # Build the binary string from the bits of found number.
        for i in range(N):
            res.append(str(num >> i & 1))

        # Reverse the string so bit significance decreases from left to right.
        res.reverse()
        return ''.join(res)
