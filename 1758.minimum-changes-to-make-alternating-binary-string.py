class Solution:
    # Approach: Greedy, Complexity: O(n), O(1)
    # Tip: There exist two alternating candidates for any string i.e. 010..101..0/1
    #      and 101..010..0/1. Chose the one that is cheaper to produce. If one
    #      alternation takes O operations, then the other takes n-O operations as
    #      one alternation needs to modify a bit that the other ignores.

    def minOperations(self, s: str) -> int:
        # ops = Operations required to turn s to 010..101..0/1
        ops = 0

        for i, ch in enumerate(s):
            # 1 and 0 shall not be at odd and even indices respectively.
            ops += 1 if (ch == '1' and i%2) or (ch == '0' and not i%2) else 0

        # Return min operations to create any of two alternating strings from s.
        return min(ops, len(s)-ops)
