#DFS
class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = [[] for _ in range(numCourses)]
        for c1,c2 in prerequisites:adjList[c2].append(c1)
        visited = set()
        stack=[]
        def hasCycle(v):
            if v in visited:
                if v in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                return False
            visited.add(v)
            stack.append(v)

            for i in adjList[v]:
                if hasCycle(i):
                    return True
            stack.pop()
            return False
        for v in range(numCourses):
            if hasCycle(v):
                return False
        return True
#bfs
class Solution:
    def canFinish(self, n, prerequisites):
        adjList = [[] for i in range(n)]
        degree = [0] * n
        queue=[]
        for c1, c2 in prerequisites:
            adjList[c2].append(c1)
            degree[j] += 1
        queue = [i for i in range(n) if degree[i] == 0]
        for i in queue:
            for j in adjList[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.append(j)
        return len(queue) == n