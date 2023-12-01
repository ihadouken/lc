class Solution:
    # Approach: Stack, Complexity: O(n), O(n)
    def removeDuplicates(self, s: str) -> str:
        # Use a stack to keep characters with no adjacent duplicates.
        stack = []

        # Loop through each character.
        for ch in s:
            # If current char = previous char (stack top), get rid of both.
            if stack and ch == stack[-1]:
                stack.pop()
            # Else, current char is not an adjacent duplicate of previous char.
            else:
                stack.append(ch)

        # Build result string with no adjacent duplicates from stack.
        s = []
        while stack:
            s.append(stack.pop())

        # Reverse result so as to cancel previous reversal due to LIFO.
        s.reverse()
        return ''.join(s)
