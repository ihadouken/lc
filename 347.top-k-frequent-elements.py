class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        buckets = [[] for _ in nums]

        for num, freq in freqs.items():
            buckets[freq-1].append(num)

        freq_sorted = []
        for bucket in reversed(buckets):
            for num in bucket:
                freq_sorted.append(num)

        return freq_sorted[:k]
