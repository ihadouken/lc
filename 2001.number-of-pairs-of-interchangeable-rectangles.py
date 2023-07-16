class Solution:
    # Approach: Hashmap, Math (Combinations), Complexity: O(n), O(n)
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_counts = {}
        change_count = 0

        # Count frequency of ratios in a hashmap.
        for length, breadth in rectangles:
            ratio = length / breadth
            ratio_counts[ratio] = ratio_counts.get(ratio, 0) + 1

        # A count x means there are x rectangles of the same of ratio. Every
        # rectangle can interchange with every other rectangle (x-1 total).
        # However, an interchange requires two rectangles so we need to divide
        # the number of interchange count by two. Therefore, for x rectangles,
        # there can be (x * (x-1)) / 2 interchanges.
        #
        # Another way is to see interchange as a combination of two. In that
        # case we will compute nC2 where nCr = fact(n) / (fact(r) * fact(n-r)).
        for count in ratio_counts.values():
            change_count += (count * (count - 1)) // 2
        return change_count
