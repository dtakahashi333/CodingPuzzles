from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
class SwapPairs:

    @staticmethod
    def solve(head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        count = 0
        while cur is not None:
            if count % 2 == 0:  # even node
                swapped = SwapPairs.swapAdjacent(cur)
                if prev is None:
                    cur = swapped
                    head = cur
                else:
                    cur = swapped
                    prev.next = cur
            prev = cur
            cur = cur.next
            count += 1

        return head

    @staticmethod
    def swapAdjacent(node: Optional[ListNode]) -> Optional[ListNode]:
        if node.next is not None:
            next_node = node.next
            node.next = next_node.next
            next_node.next = node
            return next_node

        return node
