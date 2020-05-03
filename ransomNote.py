from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicMag=defaultdict(int)
        for l in magazine:
            if dicMag.get(l):
                dicMag[l]+=1
            else:
                dicMag[l]=1
        for l in ransomNote:
            if dicMag[l]<1:
                return False
            dicMag[l]-=1
        return True