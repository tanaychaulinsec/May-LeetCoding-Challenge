from collections import defaultdict
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic=defaultdict(list)
        res=0
        for stone in S:
            if dic.get(stone):
                dic[stone]+=1
            else:
                dic[stone]=1
        for stone in J:
            if dic.get(stone):
                res+=dic[stone]
        return res        
        
        