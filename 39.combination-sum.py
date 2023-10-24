class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort input so that successive candidates needn't be checked if its found
        # that adding a candidate exceeds the target.
        candidates.sort()
        comb = []
        res = []

        def generate(reqd: int, start: int) -> None:
            # If required sum reaches zero, a perfect combination is found.
            if reqd == 0:
                res.append(comb.copy())
                return

            # Iterate over all candidates until a candidate > reqd_sum is found.
            # Recurse over every iterated candidate to find potential combinations.
            for i in range(start, len(candidates)):
                if candidates[i] > reqd:
                    return
                # Add candidate to combination and continue finding a combination
                # with updated sum.
                comb.append(candidates[i])
                generate(reqd-candidates[i], i)

                # Remove added candidate to try other candidates in its place.
                comb.pop()

        # Start with required sum = target and first candidate as the starting.
        generate(target, 0)
        return res
