class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        res=[]
        while i<len(A) and j<len(B):
            l,r=max(A[i][0],B[j][0]),min(A[i][1],B[j][1])
            if A[i][1]==r:
                i+=1
            else:
                j+=1
            if l<=r:
                res.append((l,r))
        return res