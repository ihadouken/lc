class Solution:
    # Approach: Stack, Complexity: O(n), O(n)
    def decodeString(self, s: str) -> str:
        # res holds a substring as it is decoded.
        res = []
        repeat = []
        stack = []
        top = -1

        # Read each char in encoded string.
        for ch in s:
            # Digits strings must be concatenated to get the multiplier.
            if ch.isdigit():
                repeat += ch

            # Char next to opening bracket is first char of encoded substring.
            elif ch == '[':
                # Store part of parent substring decoded until this point and
                # multiplier of substring which will now start decoding.
                stack.append([res, int(''.join(repeat))])
                res = []
                repeat = []

            # Closing bracket means substring has been decoded. Multiply it by
            # the stored multiplier and concat it with the parent substring.
            elif ch == ']':
                res *= stack[top][1]
                res = stack.pop()[0] + res

            # If a letter is encountered, append it to decoded substring.
            else:
                res += ch

        # Return string containing all substring completely decoded.
        return ''.join(res)
