class Solution:
    # Approach: Bit Hacks + Hashmap, Complexity: O(4^n), O(4^n)
    def maxProduct(self, s: str) -> int:
        res = 0
        pali, N = {}, len(s)

        # Iterate over all (2^n) subsequences of a string. The kth bit in bitmask
        # tells if the kth character (in input string) from the end is present in
        # the subsequence or not. It ranges from 0 (no characters in subsequence)
        # to 2^n - 1 (all characters in subsequence).

        # Loop Complexity: O(n * 2^n)
        for bitmask in range(1 << N):
            subseq = ""

            # Access each bit in the bitmask and build the subsequence by putting
            # the character associated with each set bit.
            for i in range(N):
                if bitmask & 1 << i:
                    subseq += s[i]

            # Store the subsequence if its a palindrome.
            if subseq == subseq[::-1]:
                pali[bitmask] = subseq

        # For each stored palindromic subsequence, iterate over all the other
        # palindromic subsequences to find pairs that are mutually disjoint.
        # The maximum product of length for such a pair is maintained.

        # Loop Complexity: O(2^n * 2^n) i.e. O(4^n)
        for p1 in pali:
            for p2 in pali:
                if not p1 & p2:
                    res = max(res, len(pali[p1]) * len(pali[p2]))

        return res
