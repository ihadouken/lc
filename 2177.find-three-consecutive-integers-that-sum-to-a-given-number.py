class Solution:
    # Approach: Math, Complexity: O(1)
    # Tip: One of the solutions to a + b + c = x is a = b = c = x/3. Rewriting
    #      the left hand side such that a, b and c are consecutive yields,
    #      (x/3 - 1) + (x) + (x/3 + 1) = x.

    #      a -> x/3 - 1
    #      b -> x/3
    #      c -> x/3 + 1

    def sumOfThree(self, num: int) -> List[int]:
        # The above explained solution can be returned if x/3 is an integer.
        if (num % 3 == 0):
            return [num // 3 - 1, num // 3, num // 3 + 1]
        return []
