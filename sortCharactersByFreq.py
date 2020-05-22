#Solution 1(Using Sort):
class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        res=""
        for i in s:
            if dic.get(i):
                dic[i]+=1
            else:
                dic[i]=1
        sorted_d = dict(sorted(dic.items(), key=operator.itemgetter(1),reverse=True))
        for char,freq in sorted_d.items():
            res+=char*freq
        return res


#Solution 2(Using Heap):

from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        counterMap=Counter(s)
        heap=[]
        res=""
        for char,freq in counterMap.items():
            heapq.heappush(heap,(-freq,char))
        while heap:
            freq,char=heapq.heappop(heap)
            res+=char * -freq
        return res

#Solution 3(most_common()):

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counterMap=Counter(s)
        res=""
        for char ,freq in counterMap.most_common():
            res+=char * freq
        return res