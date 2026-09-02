# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        x = True
        if p is None and q is None:
            return True and x
        elif p is None or q is None:
            x = False
            return False and x
        if p.val != q.val:
            x = False
            return False and x
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        return True and left and right and x

        isSame(p, q)
        return x