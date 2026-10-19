# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # unsure if import is needed for leetcode problems
        # BFS is a more natural apporahc to this tree problems so I think its worth learnign the bfs
        q = collections.deque()
        q.append(root) # append the root so that our while q will actiavte :)
        maxDepth = 0 # maybe 1 cuz we do the add 1 at the end for the final answer
        if not root:
            return 0
        # q = [1] fifo
        while q:
            current_length = len(q)
            
            

            for _ in range(current_length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            #node = [] # or the level/row thingy gotta see and learn

            maxDepth+=1
        return maxDepth
