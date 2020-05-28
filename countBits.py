class Solution:
    def countBits(self, num: int) -> List[int]:
        for i in range(num+1):
            if i==0:res=[i]
            else:
                res.append(res[i&(i-1)]+1)
        return res