class Solution:
    # Approach: Hashmap + Hashset, Complexity: O(n), O(n)
    # Note: Assuming the characters are all lowercase alphabets, complexity of
    #       the inner loop is O(1) as it traverses the hashset which can
    #       contain max 26 characters.
    # Tip: The special thing about length 3 palindromes is that the first and
    #      last characters have to be same. The middle/second element may be
    #      anything.

    def countPalindromicSubsequence(self, s: str) -> int:
        # The idea is to use hash tables to know what elements are present on
        # the left and right of the character currently in observation.
        left_chars, right_chars = set(), {}
        unique_pali = set()

        # Use a hashmap instead of hashset to store character counts on the
        # right because if there are multiple instances of a character to the
        # right, on passing this character during traversal it is not necessarily
        # known that there are no more of this character.
        for ch in s:
            right_chars[ch] = right_chars.get(ch, 0) + 1

        for ch in s:
            # However it is known that there will be one less of this character
            # to the right. So, decrement the count and if it becomes zero get
            # rid of it from the map as there will be no instances of this
            # character left on the right.
            if right_chars[ch] == 1:
                right_chars.pop(ch)
            else:
                right_chars[ch] -= 1

            # For every (unique) character on the left, try to find an instance
            # of this character on the right of the current character.
            for left in left_chars:
                # If it exists, length-3 palindrome has been found. Put found
                # palindromes in a set for the uniqueness condition.
                if left in right_chars:
                    unique_pali.add(left+ch+left)

            left_chars.add(ch)
        # Then, return the length of this set.
        return len(unique_pali)
