from typing import List, Optional
from unittest import TestCase
from swap_pairs import SwapPairs, ListNode


def listToListNode(lst: List[int]) -> Optional[ListNode]:
    head, node = None, None
    for i in range(len(lst)):
        if head is None:
            head = ListNode(lst[i])
            node = head
        else:
            node.next = ListNode(lst[i])
            node = node.next
    return head


def listNodeToList(head: Optional[ListNode]) -> List[int]:
    lst = []
    node = head
    while node is not None:
        lst.append(node.val)
        node = node.next
    return lst


class TestSwapPairs(TestCase):

    def test_solve(self):
        head = [1, 2, 3, 4]
        expected = [2, 1, 4, 3]
        self.assertListEqual(expected, listNodeToList(SwapPairs.solve(listToListNode(head))))
        head = []
        expected = []
        self.assertListEqual(expected, listNodeToList(SwapPairs.solve(listToListNode(head))))
        head = [1]
        expected = [1]
        self.assertListEqual(expected, listNodeToList(SwapPairs.solve(listToListNode(head))))
        head = [1, 2, 3]
        expected = [2, 1, 3]
        self.assertListEqual(expected, listNodeToList(SwapPairs.solve(listToListNode(head))))
