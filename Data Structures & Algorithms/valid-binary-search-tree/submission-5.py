class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, min_val, max_val):
            if not root:
                return True

            if root.left:
                if root.left.val >= root.val or root.left.val <= min_val:
                    return False

            if root.right:
                if root.right.val <= root.val or root.right.val >= max_val:
                    return False

            left = valid(root.left, min_val, root.val)
            right = valid(root.right, root.val, max_val)

            return left and right

        return valid(root, float('-inf'), float('inf'))