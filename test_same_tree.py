from typing import Optional
from unittest import TestCase
from same_tree import SameTree, TreeNode


class TestSameTree(TestCase):

    @classmethod
    def genTree(cls, items) -> Optional[TreeNode]:
        n = len(items)
        if n == 0:
            return None
        root = TreeNode(items[0])
        frontiers = [root]
        i = 1
        while len(frontiers) > 0 and i < n:
            cur = frontiers.pop(0)
            if items[i] is not None:
                cur.left = TreeNode(items[i])
                frontiers.append(cur.left)
            i = i + 1
            if i < n and items[i] is not None:
                cur.right = TreeNode(items[i])
                frontiers.append(cur.right)
            i = i + 1
        return root

    def test_solve1(self):
        p = TestSameTree.genTree([1, 2, 3])
        q = TestSameTree.genTree([1, 2, 3])
        expected = True
        self.assertEqual(expected, SameTree.solve(p, q))

    def test_solve2(self):
        p = TestSameTree.genTree([1, 2])
        q = TestSameTree.genTree([1, None, 2])
        expected = False
        self.assertEqual(expected, SameTree.solve(p, q))

    def test_solve3(self):
        p = TestSameTree.genTree([1, 2, 1])
        q = TestSameTree.genTree([1, 1, 2])
        expected = False
        self.assertEqual(expected, SameTree.solve(p, q))
