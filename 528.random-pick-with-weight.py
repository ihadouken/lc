# Approach: Binary Search, Prefix Sum, Math (Probability)
# Tip: Visualize the weights array as a continuous line of unit weights. A weight
#      of value N appends N unit weights to the line. Randomly select one of the
#      unit weights. Return the index of the weight to which the unit belongs.

#      Every unit weight has equal probability of selection. But weight supplying
#      more unit weights has higher probability of being selected ultimately.

#      Selection probability of weight = unit weights supplied / total units i.e.
#      weight[i] / sum(weights)

class Solution:
    # Complexity: O(n), O(1)
    # Prefix of weights acts as search space for binary search later.
    def __init__(self, w: List[int]):
        self.w = w
        self.pref = []

        for wi in w:
            if not self.pref:
                self.pref.append(wi)
            else:
                self.pref.append(self.pref[-1]+wi)


    # Complexity: O(logn), O(1)
    def pickIndex(self) -> int:
        # Select a random unit weight.
        rand_unit = random.randint(1, self.pref[-1])
        l, r = 0, len(self.pref) - 1

        # Binary Search to find weight that provides the selected unit.
        while l <= r:
            m = l + (r - l) // 2
            if self.pref[m] < rand_unit:
                l = m + 1
            elif self.pref[m] > rand_unit:
                r = m - 1
            else:
                l = m
                break

        # If rand_weight is not in prefix, search fails with l = index of value
        # just higher. If found, l is deliberately set to found index.
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
