class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Two hash maps to emulate bijective (one-one and onto) relation.
        pattern_map = {}
        reverse_map = {}

        i = 0
        word = ""

        for ch in pattern:
            # Get next word from s.
            while(i < len(s) and s[i] != ' '):
                word += s[i]
                i += 1

            # Check if bijection is maintained.
            if ((ch in pattern_map and pattern_map[ch] != word)
                or (word in reverse_map and reverse_map[word] != ch)):
                return False

            pattern_map[ch] = word
            reverse_map[word] = ch

            # Ready for next word.
            i += 1
            word = ""

        # Check if there was enough pattern string to match all words in s.
        # One is added to len(s) as after getting a word we increment our 
        # pointer and this will also occur for last word.
        return i == len(s) + 1
