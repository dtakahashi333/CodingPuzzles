from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
class MaxDepthOfBinaryTree:

    @classmethod
    def solveByBFS(cls, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        frontiers = [(root, 1)]
        max_depth = 0
        while len(frontiers) > 0:
            cur = frontiers.pop(0)
            left = cur[0].left
            right = cur[0].right
            depth = cur[1]
            if depth > max_depth:
                max_depth = depth
            if left is not None:
                frontiers.append((left, depth + 1))
            if right is not None:
                frontiers.append((right, depth + 1))
        return max_depth

    @classmethod
    def solveByDFS(cls, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # Recursive DFS to calculate the depth of the left and right subtrees
        left_depth = cls.solveByDFS(root.left)
        right_depth = cls.solveByDFS(root.right)
        # The max depth is the greater of the left or right subtree depth plus 1 for the current node
        return max(left_depth, right_depth) + 1
