class Solution:
    # Approach: Stack, Complexity: O(n), O(n)
    def simplifyPath(self, path: str) -> str:
        # Extract the path components between slash symbols into an array.
        components = path.split('/')

        # Maintain stack for path components of canonical path.
        stack = []
        res = []

        # Iterate over each path component.
        for comp in components:
            # If there is a '..', the canonical path wont contain the last dir.
            if stack and comp == '..':
                stack.pop()

            # Remember each directory path component. Keep track of most recent.
            elif comp != '' and comp != '..' and comp != '.':
                stack.append(comp)

        # Build canonical path, using the components stored in stack.
        while stack:
            res.append(stack.pop())
            res.append('/')

        # If the path is empty, return the root directory as path.
        if not res:
            return '/'

        # Cancel the reversal caused by LIFO operation and concat all components.
        res.reverse()
        return ''.join(res)
