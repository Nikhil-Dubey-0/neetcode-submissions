class Solution():
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        stack = [root]
        heights = {}
        diameter = 0

        while stack:
            node = stack[-1]

            if node.left and node.left not in heights:
                stack.append(node.left)

            elif node.right and node.right not in heights:
                stack.append(node.right)

            else:
                stack.pop()

                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                diameter = max(
                    diameter,
                    left_height + right_height
                )

                heights[node] = 1 + max(
                    left_height,
                    right_height
                )

        return diameter