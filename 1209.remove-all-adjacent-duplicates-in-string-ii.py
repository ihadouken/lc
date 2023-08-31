class Solution:
    # Approach: Stack, Complexity: O(n), O(n)
    def removeDuplicates(self, s: str, k: int) -> str:
        # Store seen chars along with count of adjacent duplicates in stack.
        stack = []
        top = -1

        # Process each char in string.
        for ch in s:
            # If same char is repeated immediately, increment adjacent duplicate count.
            if stack and ch == stack[top][0]:
                stack[top][1] += 1
            # If a different char is seen (or there are no entries in stack),
            # create a new stack entry for it with adjacent duplicate count of 1.
            else:
                stack.append([ch, 1])

            # If the adjacent duplicate have reached their limit, delete the
            # stack entry so that all the duplicates are not included in result.
            if stack[top][1] == k:
                stack.pop()

        res = []
        while stack:
            # Build the output by adding char in each stack entry as many times
            # as its adjacent count.
            ch, freq = stack.pop()
            for _ in range(freq):
                res.append(ch)

        # Reverse result to cancel the reversal due to LIFO travesal of stack.
        res.reverse()
        return ''.join(res)
