class Solution:
    # Approach: Monotonic Stack + Greedy, Complexity: O(n), O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        # Use a monotonic stack to store increasing digits from the left.
        stack, res = [], []
        i, TOP = 0, -1

        # Process each digit from most to least significant.
        while i < len(num):
            # Remove all digits larger than current until removal operations are
            # exhausted or there are no digits left to remove in the stack.
            if k and stack and stack[TOP] > num[i]:
                stack.pop()
                k -= 1

            # Add an element if its higher than the top. If stack is empty,
            # add element if its non-zero.
            else:
                if stack or (not stack and num[i] != '0'):
                    stack.append(num[i])
                i += 1

        # Use any non used removal operations on the stack.
        while stack and k:
            stack.pop()
            k -= 1

        # Build the result string from the stack.
        while stack:
            res.append(stack.pop())

        # Reverse the result to cancel reversal due to LIFO operation.
        res.reverse()
        if not res:
            return "0"
        return ''.join(res)
