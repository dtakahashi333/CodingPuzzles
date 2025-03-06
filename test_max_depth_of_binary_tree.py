from unittest import TestCase
from typing import Optional
from max_depth_of_binary_tree import MaxDepthOfBinaryTree, TreeNode


class TestMaxDepthOfBinaryTree(TestCase):

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

    def test_solveByBFS1(self):
        root = TestMaxDepthOfBinaryTree.genTree([3, 9, 20, None, None, 15, 7])
        expected = 3
        self.assertEqual(expected, MaxDepthOfBinaryTree.solveByBFS(root))

    def test_solveByBFS2(self):
        root = TestMaxDepthOfBinaryTree.genTree([1, None, 2])
        expected = 2
        self.assertEqual(expected, MaxDepthOfBinaryTree.solveByBFS(root))

    def test_solveByDFS1(self):
        root = TestMaxDepthOfBinaryTree.genTree([3, 9, 20, None, None, 15, 7])
        expected = 3
        self.assertEqual(expected, MaxDepthOfBinaryTree.solveByDFS(root))

    def test_solveByDFS2(self):
        root = TestMaxDepthOfBinaryTree.genTree([1, None, 2])
        expected = 2
        self.assertEqual(expected, MaxDepthOfBinaryTree.solveByDFS(root))
