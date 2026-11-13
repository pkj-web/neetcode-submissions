class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par): # parent need for undirected graph

            if node in visit: # cycle detection
                return False

            visit.add(node) # add to the set the node

            for i in adj[node]: # i == neighbor,  we iterate through the neighbors
                if i == par: # 1 == -1, no so we move on, we check if neighbor/i is the parent. parent is the key above the current row we are on.
                    continue # Skip the node we came from (avoid going backward along the same edge)

                if not dfs(i, node): # recuirsive call for now i/node turns to 1 and par is the node for par is now 0
                    return False # passing the failure upward

            return True # passing the passing upward

        return dfs(0, -1) and len(visit) == n # No cycles and all nodes visited (graph is connected)