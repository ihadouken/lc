class Solution:
    # Approach: Hashmap, Complexity: O(n), O(n)
    # Tip: Since unlimited subarray reverse operations can be used, any pair of
    #      elements can be swapped by repeated subarray reversals between the
    #      elements. So check if every element in arr has a counterpart in target
    #      i.e. arr must be permutation of target. 

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr_count = {}
        for num in arr:
            arr_count[num] = arr_count.get(num, 0) + 1

        for num in target:
            if num not in arr_count:
                return False

            if arr_count[num] == 1:
                arr_count.pop(num)
            else:
                arr_count[num] -= 1

        return not arr_count
