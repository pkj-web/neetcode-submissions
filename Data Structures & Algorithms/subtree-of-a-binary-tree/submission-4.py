class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return False

        if not root:
            return False

        if root.val == subRoot.val:
            if self.isSametree(root, subRoot):
                return True

        left_result = self.isSubtree(root.left, subRoot)
        right_result = self.isSubtree(root.right, subRoot)

        return left_result or right_result

    def isSametree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        left_same = self.isSametree(p.left, q.left)
        right_same = self.isSametree(p.right, q.right)

        return left_same and right_same