class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Hacky Solution: Find frequencies of desired characters. Then, find
        #                 the minimum frequency as it limits the construction
        #                 of word instances. Divide frequencies of 'l' and 'o'
        #                 by two as two instances of each of these are required
        #                 to form "balloon".

        # chcounts = {ch: 0 for ch in "balon"}
        #
        # for ch in text:
        #     if ch in chcounts:
        #         chcounts[ch] += 1
        #
        # chcounts['l'] //= 2
        # chcounts['o'] //= 2
        #
        # return min(chcounts.values())

        # Elegant solution: Find the frequency of every alphabet in text. Then,
        #                   find how many words may be constructed by these
        #                   frequencies by dividing the actual frequency of letter
        #                   by the required frequency.

        # allCount = Counter(text)
        # requiredCount = Counter("balloon")
        # # Total balloon instances possible can't exceed the characters in the text.
        # instances = len(text)
        #
        # for ch in requiredCount:
        #     instances = min(instances, allCount[ch] // requiredCount[ch])
        # return instances

        # Elegant solution without built-in code.
        textCounts = {chr(alpha):0 for alpha in range(ord('a'), ord('z')+1)}
        requiredCounts = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }

        for ch in text:
            if ch in textCounts:
                textCounts[ch] += 1

        instances = len(text)
        for ch in requiredCounts:
            instances = min(instances, textCounts[ch] // requiredCounts[ch])
        return instances
