# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        arr = []

        def dfs(node):
            
            if not node:
                return 0

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)


        
        dfs(root)
        return arr[k-1] # 1 2 3, if one index then arr[1] should be reuting 1 but its returing 2 it seems to be keeing the old 2 1 3 format