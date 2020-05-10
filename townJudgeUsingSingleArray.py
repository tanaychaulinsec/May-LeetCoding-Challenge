class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1 and not trust:
            return 1
        dic={}
        for i, j in trust:
            dic[i] = -1
            if j in dic:
                dic[j] += 1
            else:
                dic[j]=1
        for k in dic.keys():
            if dic[k] == N - 1:
                return k
        return -1