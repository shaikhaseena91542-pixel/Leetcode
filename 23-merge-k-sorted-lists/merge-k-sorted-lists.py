import heapq


class Solution:
    def mergeKLists(self, lists):
        min_heap = []

        # Add the first node of each linked list
        for index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(min_heap, (node.val, index, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            value, index, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            # Add the next node from the same linked list
            if node.next is not None:
                heapq.heappush(
                    min_heap,
                    (node.next.val, index, node.next)
                )

        return dummy.next