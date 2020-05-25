def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        la,lb=len(A),len(B)
        dp=[0]*(lb+1)
        for i in range(la):
            for j in range(lb-1,-1,-1):
                if A[i]==B[j]:
                    dp[j+1]=dp[j]+1
            for j in range(lb):
                dp[j+1]=max(dp[j+1],dp[j])
        return dp[lb]