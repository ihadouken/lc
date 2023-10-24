class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Array to store current combination.
        comb = []
        res = []

        def generate(start: int) -> None:
            # Combination can only have max. k elements.
            if len(comb) == k:
                res.append(comb.copy())
                return

            # Iterate over start and all numbers after it till (and including) n.
            # Further, recurse over all these numbers to find valid combinations.
            for val in range(start+1, n+1):
                comb.append(val)
                generate(val)
                # After iterating, undo the number added to try other successive
                # numbers at its position.
                comb.pop()

        # Generate has to called on 0 and not 1 to iterate over [1,n] in the first
        # level of recursive tree. This is the reason start is off by +1.
        generate(0)
        return res
