# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Approach: Two Pointer, Complexity: O(m+n), O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = 0
        n = 0

        # Find the length of both lists.
        cur = headA
        while cur:
            cur = cur.next
            m += 1

        cur = headB
        while cur:
            cur = cur.next
            n += 1

        # Identify which list is longer and which one is shorter.
        if m > n:
            longer = headA
            shorter = headB
        else:
            shorter = headA
            longer = headB

        # Move the pointer to the longer list such that both lists have equal
        # number of nodes remaining till end i.e. the length of shorter list.
        for _ in range(abs(m-n)):
            longer = longer.next

        # Continue moving both pointers until they point to a common node.
        while (longer != shorter):
            longer = longer.next
            shorter = shorter.next

        # Return the intersection point. If there is no intersection, the
        # pointers will point at NULL at the same time at the end. Thus, NULL is
        # the intersection in that case.
        return longer

    # Approach: Hashset, Complexity: O(m+n), O(m)
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # # Remember all nodes seen while traversing List A in a set. 
        # nodesA = set()
        # while headA:
            # nodesA.add(headA)
            # headA = headA.next

        # while headB:
            # # The first node common in A and B, is the intersection point.
            # if headB in nodesA:
                # return headB
            # headB = headB.next
        # # If there is no common node, there is no intersection.
        # return None
