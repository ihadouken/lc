class Solution:
    def f(self, s: str) -> int:
        smallest = s[0]
        count = 0

        for ch in s:
            if ch == smallest:
                count += 1
            elif ch < smallest:
                smallest = ch
                count = 1

        return count

    # Approach: Hashmap, Complexity: O((m+n) * s), O(s)
    # m -> number of queries
    # n -> number of words
    # s -> maximum size of word
    # Tip: 

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # Map every found smallest character frequency -> number of words with
        # that frequency.
        counts = {}

        for word in words:
            # Compute f(word[i]) and increment count for found frequency.
            freq = self.f(word)
            counts[freq] = counts.get(freq, 0) + 1

        # Process each query.
        for i, query in enumerate(queries):
            # Find f(query) to compare it with word frequences in hashmap later.
            threshold = self.f(query)
            # Overwrite every query with its result.
            queries[i] = 0

            # Iterate over all word frequencies stored in hashmap.
            for freq, count in counts.items():
                # Check if word frequency > f(query) exists.
                if freq > threshold:
                    # Increment query result by count of words with that frequency.
                    queries[i] += count

        # Return the array of query results.
        return queries

    # Approach: Brute Force, Complexity: O(n*s + m*n), O(1) where,
    # def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    #     for i, word in enumerate(words):
    #         words[i] = self.f(word)
    #
    #     for i, query in enumerate(queries):
    #         threshold = self.f(query)
    #         valid_words = 0
    #
    #         for word_smallest_count in words:
    #             if word_smallest_count > threshold:
    #                 valid_words += 1
    #
    #         queries[i] = valid_words
    #     return queries
