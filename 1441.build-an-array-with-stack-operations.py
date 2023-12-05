class Solution:
    # Approach: Two Pointer, Complexity: O(m), O(1)
    # where, m -> max (i.e. last) element in target.

    def buildArray(self, target: List[int], n: int) -> List[str]:
        # One pointer holds element of target to find in stream and other holds
        # the number read from stream.
        i, cur = 0, 1
        # Output array to keep track of operations.
        ops = []

        # Continue until all elements of target are found in stream.
        while i < len(target):
            # If number read from stream = element to be found i.e target[i],
            # push it onto the stack.
            if (target[i] == cur):
                ops.append('Push')
                i += 1
            # If number read is not the desired number, push it then pop it.
            # The desired number lies among the yet unvisited part of stream.
            else:
                ops.append('Push')
                ops.append('Pop')

            # Visit the next number in the stream.
            cur += 1

        # Return the sequence of operations used.
        return ops
