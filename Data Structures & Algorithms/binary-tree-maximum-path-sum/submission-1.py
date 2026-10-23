class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            left_result = dfs(node.left)
            right_result = dfs(node.right)

            left_max = max(left_result, 0)
            right_max = max(right_result, 0)

            res[0] = max(res[0], node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]