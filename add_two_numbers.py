# Definition for singly-linked list.
from typing import Optional


# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:

    @staticmethod
    def solve(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = None
        carry_over = 0

        while True:
            if l1 is None and l2 is None:
                if carry_over != 0:  # Extra node for a carry over.
                    node.next = ListNode()
                    node.next.val = carry_over
                return head

            if node is None:
                node = ListNode()
                head = node
            else:
                node.next = ListNode()
                node = node.next

            if l1 is not None and l2 is not None:
                node.val = l1.val + l2.val + carry_over
                # Move to the next digit.
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                node.val = l1.val + carry_over
                # Move to the next digit.
                l1 = l1.next
            elif l2 is not None:
                node.val = l2.val + carry_over
                # Move to the next digit.
                l2 = l2.next

            # Carry over
            if node.val >= 10:
                carry_over = 1
                node.val = node.val % 10
            else:
                carry_over = 0
