# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap first and second
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev two nodes ahead
            prev = first

        return dummy.next