# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class RemoveNthFromEnd:

    @staticmethod
    def solve(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get the length of the linked list.
        node = head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        if count == 1 and n == 1:
            return None
        m = count - n + 1
        # Move to the node to be deleted.
        node, prev = head, None
        for _ in range(1, m):
            prev = node
            node = node.next
        if node.next is None:
            prev.next = None
        else:
            node.val = node.next.val
            node.next = node.next.next
        return head
