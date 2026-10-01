# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return False

        if not root:
            return False
        
        if root.val == subRoot.val:
            if (self.isSametree(root,subRoot)):
                return True
        
        x = self.isSubtree(root.left, subRoot)

        y = self.isSubtree(root.right, subRoot)

        return x or y
    
    def isSametree(self, p, q):


        

        if not p and not q:
            return True
        
        if not p or not q:
            
            return False
        if p.val != q.val:
            return False
        x = self.isSametree(p.left, q.left)
        y = self.isSametree(p.right, q.right)

        return x and y
        