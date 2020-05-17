class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        DicP=collections.Counter(p)
        res=[]
        DicS={}
        for i in range(len(s)):
            if s[i] in DicS:
                DicS[s[i]]+=1
            else:
                DicS[s[i]]=1
            
            if i>len(p)-1:
                DicS[s[i-len(p)]]-=1
            if DicS[s[i-len(p)]]==0:
                    del DicS[s[i-len(p)]]
            if DicP==DicS:
                res.append(i-(len(p)-1))
        return res