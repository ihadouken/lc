class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Record frequencies in a hashmap
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        # Approach: Bucket Sort - Time: O(n), Space: O(n)
        # Reasons:
        # 1 <= frequency of an element existing in list <= size of list.
        # Each bucket represents a frequency.
        # Bucket used as multiple elements may have same frequency.
        buckets = [[] for _ in nums]

        # Fill buckets with unique elements from nums.
        for num, freq in freqs.items():
            buckets[freq-1].append(num)

        # Traverse the buckets right to left to sort the elements from most
        # occuring to least occuring.
        freq_sorted = []
        for bucket in reversed(buckets):
            for num in bucket:
                freq_sorted.append(num)

        # Return the top k elements from the sorted list of unique elements.
        return freq_sorted[:k]

        # # Approach: Quickselect
        # # Time - Average: O(n^2), Worst: O(n) (depending on pivot selection)
        # # Space - O(n)
        # uniques = [num for num in freqs.keys()]
        # # Partition the list (as in quicksort) but based on decreasing frequency.
        # def partition(arr: list[int], beg: int, end: int):
        #     i = j = beg
        #     pivot = end
        #
        #     while (i < pivot):
        #         if freqs[arr[i]] > freqs[arr[pivot]]:
        #             arr[i], arr[j] = arr[j], arr[i]
        #             j += 1
        #         i += 1
        #
        #     arr[j], arr[pivot] = arr[pivot], arr[j]
        #     return j
        #
        # def quickselect(arr: list[int], beg: int, end: int) -> None:
        #     # pivot = x means the partioning put the most frequent x+1 elements upto index x.
        #     pivot = partition(arr, beg, end)
        #     # Selected less elements than required.
        #     # Now we select the remaining number of elements.
        #     if pivot < k-1:
        #         quickselect(arr, pivot+1, end)
        #     # Selected more elements than required.
        #     # Now we want a smaller and richer selection of the most frequent.
        #     elif pivot > k-1:
        #         quickselect(arr, beg, pivot-1)
        #     # Selected just the right amount, we are done.
        #     else:
        #         return
        #
        # quickselect(uniques, 0, len(uniques) - 1)
        # return uniques[:k]
