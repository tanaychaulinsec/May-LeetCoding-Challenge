class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicS1=collections.Counter(s1)
        dicS2={}
        for i in range(len(s2)):
            if s2[i] in dicS2:
                dicS2[s2[i]]+=1
            else:
                dicS2[s2[i]]=1
            if i>len(s1)-1:
                dicS2[s2[i-len(s1)]]-=1
                if dicS2[s2[i-len(s1)]]==0:
                    del dicS2[s2[i-len(s1)]]
            if dicS2==dicS1:
                return True
        return False