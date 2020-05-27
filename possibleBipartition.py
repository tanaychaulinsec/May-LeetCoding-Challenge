class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        color=[-1]*(N+1)
        for i in range(1,N+1):
            if color[i]==-1:
                color[i]=0
                q=[i]
                while q:
                    node=q.pop()
                    for j in graph[node]:
                        if color[j]==color[node]:
                            return False
                        if color[j]==-1:
                            color[j]=color[node]^1
                            q.append(j)
        return True