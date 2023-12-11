class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Use a stack to keep track of current parenthesis string.
        stack = []
        res = []

        def generate(open: int, close: int) -> None:
            # Valid string is produced on running out of closing (and opening)
            # parenthesis.
            if close == n:
                res.append(''.join(stack))
                return

            # Add an opening if its available and explore further strings.
            if open < n:
                stack.append('(')
                generate(open+1, close)
                # Undo the opening to explore strings with a closing instead.
                stack.pop()

            # Add a closing while not exceeding openings.
            if close < open:
                stack.append(')')
                generate(open, close+1)
                # Remove the closing to ultimately try a closing for last opening.
                stack.pop()

        # Call generate with empty stack and zero initial openings and closing.
        generate(0, 0)
        # Return the parenthesis subsequences recorded.
        return res
