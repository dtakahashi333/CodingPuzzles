from typing import Optional, List
from unittest import TestCase, expectedFailure
from merge_two_lists import MergeTwoLists, ListNode


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


class TestMergeTwoLists(TestCase):

    def test_solve1(self):
        list1 = listToListNode([1, 2, 4])
        list2 = listToListNode([1, 3, 4])
        expected = [1, 1, 2, 3, 4, 4]
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve(list1, list2)))

    def test_solve2(self):
        list1 = listToListNode([])
        list2 = listToListNode([])
        expected = []
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve(list1, list2)))

    def test_solve3(self):
        list1 = listToListNode([])
        list2 = listToListNode([0])
        expected = [0]
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve(list1, list2)))

    def test_solve4(self):
        list1 = listToListNode([])
        list2 = listToListNode([-5, 1])
        expected = [-5, 1]
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve(list1, list2)))

    def test_solve2_1(self):
        list1 = listToListNode([1, 2, 4])
        list2 = listToListNode([1, 3, 4])
        expected = [1, 1, 2, 3, 4, 4]
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve2(list1, list2)))

    def test_solve2_2(self):
        list1 = listToListNode([])
        list2 = listToListNode([])
        expected = []
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve2(list1, list2)))

    def test_solve2_3(self):
        list1 = listToListNode([])
        list2 = listToListNode([0])
        expected = [0]
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve2(list1, list2)))

    def test_solve2_4(self):
        list1 = listToListNode([])
        list2 = listToListNode([-5, 1])
        expected = [-5, 1]
        self.assertListEqual(expected, listNodeToList(MergeTwoLists.solve2(list1, list2)))
