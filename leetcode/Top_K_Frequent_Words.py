import collections
import heapq
class Solution:
    def topKFrequent(self, words, k):
        words.sort()
        counter=collections.Counter(words)

        ans=[]
        for i,j in counter.items():
            k=k-1
            ans.append(i)
            if k==0:
                break
        return ans

var=Solution()

print(var.topKFrequent(["G","B","S","S","A"],2))


