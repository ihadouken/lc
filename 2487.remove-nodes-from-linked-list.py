# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Approach: Monotonic Stack, Complexity: O(n), O(n)
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack = []
    #     while head:
    #         # Push nodes until a node strictly greater than top is found.
    #         if not stack or head.val <= stack[-1].val:
    #             stack.append(head)
    #             head = head.next
    #         # If a node strictly greater than top is found, remove nodes
    #         # that are smaller than it.
    #         elif stack and head.val > stack[-1].val:
    #             stack.pop()
    #
    #     # At the end, stack contains nodes that have no strictly greater nodes
    #     # to its right. Build the resultant list such that top is the tail node.
    #     # This is done by repeatedly popping and adding the nodes at the head.
    #     head = None
    #     while stack:
    #         new = stack.pop()
    #         new.next = head
    #         head = new
    #
    #     return head

    # Approach: Reversed Traversal, Complexity: O(n), O(1)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list to iterate over nodes in reversed order.
        head = self.reverse(head)
        largest = head

        # Find and delete nodes that appear after a node with higher value.
        while largest.next:
            # If a node with value smaller than largest is found, delete it.
            if largest.val > largest.next.val:
                largest.next = largest.next.next
            # If a node has value >= largest, make it the largest node.
            else:
                largest = largest.next

        # Reverse the list again on remaining nodes to undo the previous reversal.
        return self.reverse(head)

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        return prev
