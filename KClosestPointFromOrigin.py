import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        minHeap=[]
        res=[]
        for x,y in points:
            dis=(x**2)+(y**2)
            heapq.heappush(minHeap,(dis,(x,y)))
        for i in range(K):
            dis,point=heapq.heappop(minHeap)
            res.append(point)                
        return res