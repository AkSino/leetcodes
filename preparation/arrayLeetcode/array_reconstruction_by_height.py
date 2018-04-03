import heapq
class Solution():
    def reconstructQueue(self, people):
        b=[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
        a=[]
        ans=[None for i in range(len(b))]
        for each in b:
            heapq.heappush(a,each)
        while a:
            mid=heapq.heappop(a)
            count=0
            for i in range(len(ans)):
                if count==mid[1] and ans[i]==None:
                    ans[i]=mid
                    break
                if ans[i]==None or ans[i][0]==mid[0]:
                    count+=1
        return ans



