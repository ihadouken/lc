class Solution:
    # Approach: Line Sweep + Prefix Sum + ASCII Math, Complexity: O(n), O(n)
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Convert string to char string for O(1) modification.
        s = list(s)
        N = len(s)

        # Use "line" array to keep track of range increment done to s.
        line = [0] * (N+1)

        # Process every shift.
        for start, end, dir in shifts:
            # Calculate increment type (-1/+1) from shift direction (0/1).
            incr = 2 * dir - 1
            # Incr. line[start] to signify range shift starting from index "start".
            # Undo shift (negate sign to toggle type of incr.) at index "end+1" to
            # signify "end" as the last index incremented / shifted_id.
            line[start] += incr
            line[end+1] += -incr

        # Compute prefix sum so that every index has individual shift info rather
        # than just the range ends.
        for i in range(1, N):
            line[i] += line[i-1]

        # Apply corresponding shifts to each char of "s".
        for i in range(N):
            # Find the char index 0..25 after shifting char.
            shifted_id = (ord(s[i]) - ord('a') + line[i]) % 26

            # Rotate index by 26 to handle -ve index after too much reverse shift.
            if shifted_id < 0:
                shifted_id += 26

            # Overwrite char with shifted char.
            s[i] = chr(ord('a') + shifted_id)

        # Convert modified char list to string and return it.
        return ''.join(s)
