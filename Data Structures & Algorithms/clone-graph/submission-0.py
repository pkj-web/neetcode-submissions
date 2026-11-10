"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        about = {}

        about[node] = Node(node.val) # init the frist node oject clone

        q = deque([node]) #init node for tjhe orginal graph 

        while q:

            cur = q.popleft() # node object 2

            for neighbor in cur.neighbors:
                if neighbor not in about:

                    about[neighbor] = Node(neighbor.val)

                    q.append(neighbor)

                about[cur].neighbors.append(about[neighbor])

        return about[node]

        