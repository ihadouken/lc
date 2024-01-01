class Solution:
    # Approach: Sorting + Two Pointer, Complexity: O(nlogn + mlogm), O(1)
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort "s" so that smallest cookie available can be tried for allocation
        # first. Sort "g" so that cookies of increasing sizes can be allocated
        # in a single pass over "g" i.e. cookie requirements.
        s.sort()
        g.sort()

        # Set both pointers to first element in respective arrays.
        content, i, j = 0, 0, 0

        # Continue until cookies or children are exhausted.
        while i < len(s) and j < len(g):
            # If current cookie fulfills current non-content child's greed.
            if s[i] >= g[j]:
                # Increment count of content children and move on to the next
                # non-content child.
                j += 1
                content += 1

            # Either the current cookie is allocated or is thrown away.
            i += 1

        # Return count of content children.
        return content
