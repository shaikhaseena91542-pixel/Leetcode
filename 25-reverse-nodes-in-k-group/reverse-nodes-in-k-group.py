# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Dummy node simplifies handling the new head after reversal
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Check if there are at least k nodes left starting from group_prev.next
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # fewer than k nodes remain; leave as is

            group_next = kth.next  # node right after this k-group
            prev, curr = group_next, group_prev.next

            # Reverse the k nodes in this group
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect: group_prev.next was the old head of the group,
            # which is now the tail after reversal
            new_group_start = prev
            old_group_head = group_prev.next
            group_prev.next = new_group_start
            group_prev = old_group_head  # this is now the tail of the reversed group

        return dummy.next