# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoLists:

    @staticmethod
    def solve(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged, head = None, None
        while list1 is not None or list2 is not None:
            new_node = None
            if list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    new_node = ListNode(list1.val)
                    list1 = list1.next
                else:
                    new_node = ListNode(list2.val)
                    list2 = list2.next
            elif list1 is not None:
                new_node = ListNode(list1.val)
                list1 = list1.next
            elif list2 is not None:
                new_node = ListNode(list2.val)
                list2 = list2.next

            if new_node is not None:
                # If merged is empty, create a new ListNode.
                if merged is None:
                    merged = new_node
                    head = merged
                else:
                    merged.next = new_node
                    merged = merged.next

        return head

    @staticmethod
    def solve2(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Insert contents in list2 to list1.
        head = list1
        cur, prev = head, head
        while list2 is not None:
            if cur is None:
                if prev is None: # list1 is empty.
                    head = list2
                else:
                    prev.next = list2
                break
            elif cur.val >= list2.val:
                if cur == prev:  # At the head of the list
                    cur = ListNode(list2.val, cur)
                    prev, head = cur, cur
                else:
                    new_node = ListNode(list2.val)
                    prev.next = new_node
                    new_node.next = cur
                    prev = new_node
                list2 = list2.next
            else:  # list1.val < list2.val
                while cur is not None and cur.val < list2.val:
                    prev = cur
                    cur = cur.next

        return head
