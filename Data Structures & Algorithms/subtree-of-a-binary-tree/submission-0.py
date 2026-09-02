# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def isSubT(root, subRoot):
            nonlocal res
            if root is None or res:
                return

            if root.val == subRoot.val:
                stack = [(root, subRoot)]

                while stack:
                    node, subNode = stack.pop()
                    
                    if not node and not subNode:
                        continue
                    if not node or not subNode:
                        break
                    if node.val != subNode.val:
                        break

                    stack.append((node.left, subNode.left))
                    stack.append((node.right, subNode.right))

                else:
                    res = True
                    return

            isSubT(root.left, subRoot)
            isSubT(root.right, subRoot)

        isSubT(root, subRoot)
        return res


