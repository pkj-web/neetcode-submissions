class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adj = {}

        for i in range(n):
            adj[i] = []

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        def dfs(node):

            visit.add(node)

            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        
        res = 0

        for i in range(n):
            if i not in visit:
                dfs(i)
                res+=1

        return res