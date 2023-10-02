class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Extract words from list.
        res = ''
        words = text.split()

        # Num of spaces = len of original string - cummulative length of words.
        spaces = len(text) - len(''.join(words))

        # Find maximum uniform spaces between each word. Find spaces that can't
        # be accomodated and have to be added at the end.
        if len(words) > 1:
            extras = spaces % (len(words) - 1)
            spc_per_word = spaces // (len(words) - 1)
        else:
            # For a single word, add all spaces at the end.
            extras = spaces
            spc_per_word = 0

        for word in words:
            # Add uniform space to result before every word excluding the first.
            if res:
                res += ' ' * spc_per_word
            # Add word to result after adding the uniform spacing.
            res += word

        # Append extra spacing to word and return it.
        res += ' ' * extras
        return res
