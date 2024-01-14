class Solution:
    # Approach: Counting + Hashmap, Complexity: O(n), O(n)
    # Tip: For the strings to be close, they must be of equal lengths, use the
    #      same chars and have the same set of char frequencies irrespective of
    #      chars as frequencies of two chars can be swapped. Frequency of chars
    #      matters but order doesn't as infinite swaps can be made between chars
    #      in the strings.

    def closeStrings(self, word1: str, word2: str) -> bool:
        # Operations cant make strings of unequal lengths equal.
        if len(word1) != len(word2):
            return False

        ch_freq1, ch_freq2, count_freq = {}, {}, {}

        # Store frequencies of chars in word1 and word2 in separate hashmaps.
        for ch1, ch2 in zip(word1, word2):
            ch_freq1[ch1] = ch_freq1.get(ch1, 0) + 1
            ch_freq2[ch2] = ch_freq2.get(ch2, 0) + 1

        # Find frequencies of the frequencies of the chars in strings.
        for (ch1, count1), (ch2, count2) in zip(ch_freq1.items(), ch_freq2.items()):
            # Both strings should contain the same chars.
            if ch1 not in ch_freq2 or ch2 not in ch_freq1:
                return False

            # Add frequency's frequency if it appears in word1's hashmap.
            count_freq[count1] = count_freq.get(count1, 0) + 1
            # Remove frequency's frequency if it appears in word2's hashmap.
            count_freq[count2] = count_freq.get(count2, 0) - 1

        # If both strings, have the same set of char frequencies (irrespective of
        # chars), all keys have 0 value as equal +ve canceled by equal -ve.
        for freq in count_freq.values():
            if freq != 0:
                return False

        # Return true if validation process suceeds.
        return True
