class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Record frequencies in hashmap.
        freqs = {}
        for element in arr:
            freqs[element] = freqs.get(element, 0) + 1

        # Find duplicate frequency if it exists via hashset.
        unique_freqs = set()
        for freq in freqs.values():
            if freq in unique_freqs:
                return False
            unique_freqs.add(freq)

        return True
