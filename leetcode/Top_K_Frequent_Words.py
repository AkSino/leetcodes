import heapq
class Solution:
    def topKFrequent(self, words, k):
        ans={}
        heap=[]
        fin_ans=[]
        for each in words:
            if each in ans:
                ans[each]+=1
            else:
                ans[each]=1
        for each in ans:
            heapq.heappush(heap,(-ans[each],each))
        for i in range(k):
            fin_ans.append(heapq.heappop(heap)[1])
        return fin_ans


var=Solution()

print(var.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2))


