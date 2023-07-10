# Tip: Emulate a mathematical relation between the two strings and ensure that
# it is one-one.

# Complexity: O(n), where s is the length of given strings.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Hash maps to store relation sets.
        charmap = {}
        revmap = {}

        for c1, c2 in zip(s, t):
            # If both characters are not related to any other character, create
            # a relation mapping between the two.
            if c1 not in charmap and c2 not in revmap:
                charmap[c1] = c2
                revmap[c2] = c1

            # If one of them is already related, we can't have one-one.
            elif c1 not in charmap or c2 not in revmap:
                return False

            # If both are already related, check if they are actually related
            # to each other.
            else:
                if charmap[c1] != c2 or revmap[c2] != c1:
                    return False
        # There was no problem verifying one-one relationship.
        return True
