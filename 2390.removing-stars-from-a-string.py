class Solution:
    # Approach: Stack, Complexity: O(n), O(1)
    def removeStars(self, s: str) -> str:
        # Store traversed characters in stack.
        stack = []

        for ch in s:
            # If star is encountered, pop last seen character in stack.
            if ch == '*':
                stack.pop()
            # Otherwise, store the traversed character.
            else:
                stack.append(ch)

        # Build the result using characters in stack.
        res = []
        while stack:
            res.append(stack.pop())

        # Since stack is lifo, the result was created in inverse order. Reverse
        # it again and return the expected result.
        res.reverse()
        return ''.join(res)

