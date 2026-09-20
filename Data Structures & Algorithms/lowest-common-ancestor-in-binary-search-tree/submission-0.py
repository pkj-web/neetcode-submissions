# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < root.val and q.val < root.val: # p and q are left of initial root
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val: # p and q are right of intital
            return self.lowestCommonAncestor(root.right, p, q)

        else: # root is our LCA, becuase eithe one is on one side and the other is on anthor, or one of them is our LCA
            return root
        