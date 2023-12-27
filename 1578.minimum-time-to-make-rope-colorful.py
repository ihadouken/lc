class Solution:
    # Approach: Stack + Greedy, Complexity: O(n), O(n)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Use stack to store rope with distinct coloured neighbours.
        stack = []
        # Initialize removal time required to 0.
        rem_time = 0
        i = 0

        # Iterate over the rope of ballons.
        while i < len(colors):
            # If current candidate balloon conflicts with last selection.
            if stack and stack[-1][0] == colors[i]:
                # If last selected ballon is easier to remove, unselect it. Balloon
                # selected before (beneath the just removed balloon in the stack)
                # are also reviewed against the current candidate.
                if neededTime[i] > stack[-1][1]:
                    rem_time += stack.pop()[1]
                # If current candidate is easier to remove, consider next candidate.
                else:
                    rem_time += neededTime[i]
                    i += 1
            # If the current candidate creates no conflicts, add it.
            else:
                stack.append((colors[i], neededTime[i]))
                i += 1

        # Return the cummulative time required in removing balloons.
        return rem_time



