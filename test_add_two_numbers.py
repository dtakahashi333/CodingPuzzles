from typing import List, Optional
from unittest import TestCase
from add_two_numbers import AddTwoNumbers, ListNode


def list_node_to_list(head: Optional[ListNode]):
    n = head
    l = []
    while True:
        l.append(n.val)
        if n.next is None:
            return l
        else:
            n = n.next


def list_to_list_node(l: Optional[List[int]]) -> Optional[ListNode]:
    head = None
    n = None
    for v in l:
        if n is None:
            n = ListNode()
            head = n
        else:
            n.next = ListNode()
            n = n.next
        n.val = v
    return head


class TestAddTwoNumbers(TestCase):

    def test_solve1(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        expected = [7, 0, 8]
        actual = list_node_to_list(
            AddTwoNumbers.solve(
                list_to_list_node(l1),
                list_to_list_node(l2)
            )
        )
        self.assertEquals(expected, actual)

    def test_solve2(self):
        l1 = [0]
        l2 = [0]
        expected = [0]
        actual = list_node_to_list(
            AddTwoNumbers.solve(
                list_to_list_node(l1),
                list_to_list_node(l2)
            )
        )
        self.assertEquals(expected, actual)

    def test_solve3(self):
        l1 = [9, 9, 9, 9, 9, 9, 9]
        l2 = [9, 9, 9, 9]
        expected = [8, 9, 9, 9, 0, 0, 0, 1]
        actual = list_node_to_list(
            AddTwoNumbers.solve(
                list_to_list_node(l1),
                list_to_list_node(l2)
            )
        )
        self.assertEquals(expected, actual)
