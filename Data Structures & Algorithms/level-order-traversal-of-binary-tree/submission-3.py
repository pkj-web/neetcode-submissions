# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # SCREAMING BBBBBFFFFFFSSSSSSSS


        q = collections.deque()


        q.append(root)
        if not root:
            return []

        res  = []
        
        while q:
         
            level_len = len(q)

            level = []
            for _ in range(level_len):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    
                    q.append(node.left)
                    

                if node.right:
                    
                    q.append(node.right)
                    

            res.append(level) # otuisde of for loop so per  LEVEL
        return res

        '''
        Input: root = [1,2,3,4,5,6,7]

        Output: [[1],[2,3],[4,5,6,7]]
        '''
        