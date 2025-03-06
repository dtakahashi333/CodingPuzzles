from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 100. Same Tree
# https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150
class SameTree:

    @classmethod
    def solve(cls, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is not None and q is not None:
            if p.val != q.val:
                return False
            left_is_same = cls.solve(p.left, q.left)
            right_is_same = cls.solve(p.right, q.right)
            return left_is_same and right_is_same
        elif p is None and q is None:
            return True
        else:
            return False

    @classmethod
    def solveByChatGPT(cls, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # Both are None
            return True
        if not p or not q:  # One is None and the other is not
            return False
        # Check if values are the same and recursively check left and right subtrees
        return p.val == q.val and cls.solve(p.left, q.left) and cls.solve(p.right, q.right)
