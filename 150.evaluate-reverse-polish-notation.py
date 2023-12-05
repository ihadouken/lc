class Solution:
    # Approach: Stack, Complexity: O(n), O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack to store operand tokens.
        stack = []
        # Declare list of operations for convenient lookup.
        operations = {'+', '-', '/', '*'}

        # Process every token.
        for token in tokens:
            if token in operations:
                # Perform operation on two most recent operands stored in stack.
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Build the operation as a string.
                stmt = operand1 + token + operand2

                # Evaluate the operation string via python's eval BIF.
                # Conversion to int is done to round down negative fractional
                # results towards zero. Store result as it may be a future operand.
                res = int(eval(stmt))
                stack.append(str(res))

            else:
                # Store operands (numeric tokens) for future use in operations.
                # Storing as string allows easier building of operation strings.
                stack.append(token)

        # Stack contains a single entry i.e. the result after all operations.
        return int(stack[-1])
