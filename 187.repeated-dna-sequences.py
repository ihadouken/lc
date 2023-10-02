# Note: For the purpose of this problem, a "subsequence" refers to DNA subsequence
#       and not a subsequence of array/string as understood in regular DSA.

class Solution:
    # Approach: Sliding Window + Hashset, Complexity: O((n-m)*m), O((n-m)*m) where,
    # m -> length of sequence (10 in the statement), n -> length of string.

    # Each window is of size m and there are a total of n-m windows. A string is
    # built and stored for every window. Hence the TC.

    # In the worst case, each window repeats exactly once. The sets have to store all possible windows. Hence the SC.

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # If length of s < required length of sequence, it can't contain one.
        SEQ_LEN = 10
        if len(s) < SEQ_LEN:
            return []

        # Start with a window of first SEQ_LEN characters.
        l, r = 0, SEQ_LEN - 1
        seen, repeated = set(), set()

        while (r < len(s)):
            # Build the subsequence string from the window.
            seq = s[l:r+1]

            # If the subsequence is repeated, store it. Record subsequnces that
            # repeat multiple times only once.
            if seq in seen and seq not in repeated:
                repeated.add(seq)

            # Store every subsequence for checking future repetitions.
            seen.add(seq)

            # Shift the window by one char to consider the next SEQ_LEN chars.
            r += 1
            l += 1

        # Return a list of repeated DNA subsequences of given length.
        return list(repeated)
