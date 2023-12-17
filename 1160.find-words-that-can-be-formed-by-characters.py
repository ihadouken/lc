class Solution:
    # Approach: Hashmap, Counting, Complexity: O(n + k*m), O(max(n, k))
    # where, n -> size of "chars", m -> size of "words", k -> average word size.
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_count = res = 0
        ch_counts = collections.defaultdict(int)

        # Count chars in "chars".
        for ch in chars:
            ch_counts[ch] += 1
            total_count += 1

        # Iterate over the words.
        for word in words:
            # Word with more letters than total letters in "chars" can't be created.
            if len(word) > total_count:
                continue

            # Create a copy of counts for modifications.
            avail = ch_counts.copy()
            for ch in word:
                # Count chars of word in copy of counts.
                if avail[ch] == 1:
                    avail.pop(ch)
                else:
                    avail[ch] -= 1

            # No char can have count < 0 for a valid word.
            if all(count > 0 for count in avail.values()):
                # Sum lengths of valid words.
                res += len(word)

        # Return sum of lengths of valid words.
        return res
