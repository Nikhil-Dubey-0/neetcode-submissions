# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        first = True
        def dfs(root,p,q):
            nonlocal res
            nonlocal first
            if not root:
                return None
            if ((root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val)) and (first == True):
                res = root
                first = False
            dfs(root.left,p,q)
            dfs(root.right,p,q)
            return None
        dfs(root,p,q)
        return res