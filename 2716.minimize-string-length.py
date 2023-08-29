class Solution:
    # Approach: Hashmap, Complexity: O(n), O(n)
    # Tip: Instead of checking if a left and right occurence exists for a middle
    #      character, check if the middle occurence exists for left occurence
    #      and a right occurence exists for the middle occurence.

    def minimizedStringLength(self, s: str) -> int:
        newlen = len(s)
        counts = {}

        # Count each 
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in s:
            # Decrement count of occurences current character and remove it from
            # counts if it was the only occurence left. This prevents current
            # character being assumed as its own duplicate.
            if counts[ch] == 1:
                counts.pop(ch)
            else:
                counts[ch] -= 1

            # If a duplicate exists to char's right, the char can be deleted.
            if ch in counts:
                newlen -= 1

        # Return the minimized length.
        return newlen
