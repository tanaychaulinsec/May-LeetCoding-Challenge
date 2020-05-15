class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        totalSum,maxSum,curMax,minSum,curMin=sum(A),-float('inf'),0,float('inf'),0
        for num in A:
            curMax=max(num,curMax+num)
            maxSum=max(curMax,maxSum)
            
            curMin=min(num,curMin+num)
            minSum=min(curMin,minSum)
        return max(maxSum,totalSum-minSum) if maxSum>0 else maxSum
            