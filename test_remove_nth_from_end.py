from unittest import TestCase
from remove_nth_from_end import RemoveNthFromEnd, ListNode


class TestRemoveNthFromEnd(TestCase):

    def test_solve1(self):
        node = ListNode(5)
        node = ListNode(4, node)
        node = ListNode(3, node)
        node = ListNode(2, node)
        head = ListNode(1, node)
        n = 2
        expected = [1, 2, 3, 5]
        head = RemoveNthFromEnd.solve(head, n)
        result = []
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next
        self.assertListEqual(expected, result)

    def test_solve2(self):
        head = ListNode(1)
        n = 1
        expected = []
        head = RemoveNthFromEnd.solve(head, n)
        result = []
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next
        self.assertListEqual(expected, result)

    def test_solve3(self):
        node = ListNode(2)
        head = ListNode(1, node)
        n = 1
        expected = [1]
        head = RemoveNthFromEnd.solve(head, n)
        result = []
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next
        self.assertListEqual(expected, result)

    def test_solve4(self):
        node = ListNode(3)
        node = ListNode(2, node)
        head = ListNode(1, node)
        n = 3
        expected = [2, 3]
        head = RemoveNthFromEnd.solve(head, n)
        result = []
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next
        self.assertListEqual(expected, result)
