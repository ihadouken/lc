# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach: Hashset, Complexity: O(n), O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Empty list can't have a cycle.
        if not head:
            return False

        # Record the addresses of nodes seen already in hashmap.
        seen = set()

        # Iterate over the nodes.
        while head:
            # If node is already seen before, it is the entry point to cycle.
            if id(head) in seen:
                return True
            # Remember this traversed node and move on to the next one.
            seen.add(id(head))
            head = head.next
        # If no node was seen twice during the traversal, there is no cycle.
        return False
