class Solution:
    def firstUniqChar(self, s: str) -> int: 
        dic={}
        for ch in s:
            if dic.get(ch):
                dic[ch]+=1
            else:
                dic[ch]=1
        for index,ch in enumerate(s):
            if dic.get(ch) and dic[ch]==1:
                return index
        return -1