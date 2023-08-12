# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty list requires no processing.
        if not head:
            return head

        # Use arrays to store even and odd nodes.
        even = []
        odd = []
        # Use a flag to alternate node addition in even or odd.
        flag = 1
        # Initialize result linked list by adding first odd node.
        newhead = newtail = head
        head = head.next

        while head:
            if flag == 1:
                even.append(head)
            else:
                odd.append(head)

            # Reverse flag to add alternately to even/odd lists.
            flag *= -1
            # Move on to the next node.
            head = head.next

        # Append all odd nodes to result list.
        for node in odd:
            newtail.next = node
            newtail = node

        # Append all even nodes to result list after the odd ones.
        for node in even:
            newtail.next = node
            newtail = node

        # Terminate the list after adding even nodes and return it.
        newtail.next = None
        return newhead
