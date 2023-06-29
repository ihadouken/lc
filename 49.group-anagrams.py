"""
Approach: sort all the given strings then group indices with same string as
value of hashmap whose key is the sorted string. A group indices of is equivalent
to a group of anagrams in the original string list. Traverse the hashmap putting
each strings of a anagram group in a list. Put all these lists in a another list
to get the result.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agroups = []
        anagrams = {}

        # O(n * k * logk)
        sorted_strs = [''.join(sorted(s)) for s in strs]
        # O(n * k)
        for i, s in enumerate(sorted_strs):
            # O(k)
            if s not in anagrams:
                anagrams[s] = [i]
            # O(1)
            else:
                anagrams[s].append(i)

        # O(n)
        for occurences in anagrams.values():
            # O(1)
            group = [strs[occurence] for occurence in occurences]
            agroups.append(group)

        return agroups
