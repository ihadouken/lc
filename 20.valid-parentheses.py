class Solution:
    # Approach: Stack, Complexity: O(n), O(n)
    def isValid(self, s: str) -> bool:
        # Use a stack to store tokens. Push opening symbols as seen and pop
        # those opening symbols when closing symbols are encountered.
        stack = []

        for ch in s:
            # Append unconditionally any opening symbols as we can't know the
            # validity right now.
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)

            # When a closing symbol is encountered, check if we are closing the
            # right delimiter (using the stack's top) or if there was even one
            # (by checking if the stack is empty).
            elif ch == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif ch == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif ch == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()

        # If the input was valid every opening will be popped by some closing
        # symbol meaning the stack will return to its initial state i.e. empty.
        return not stack
