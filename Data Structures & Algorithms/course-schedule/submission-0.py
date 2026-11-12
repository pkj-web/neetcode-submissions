class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {}

        for i in range(numCourses):
            preMap[i] = []


        for i,j in prerequisites:
            preMap[i].append(j)

        #print(preMap)

        visiting = set()

        def dfs(node):
            if node in visiting:
                return False # cycle

            if preMap[node] == []:
                return True # no cycle


            visiting.add(node)
            for i in preMap[node]:
                if not dfs(i):
                    return False

            visiting.remove(node)
            preMap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True