# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # exact same structure
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        
        # exact same values
        if p.val != q.val:
            return False

        # return True if sameTree, else False

        x = self.isSameTree(p.left, q.left)
        y = self.isSameTree(p.right, q.right)

        return x and y
        