class Solution:
    def hIndex(self, citations):
        if (len(citations) == 0):
            return 0
        citations.sort()
        ans=0
        for i in range(len(citations)):
            if (len(citations) - i <= citations[i]):
                if(i==0):
                    ans=len(citations)
                    break
                elif(citations[i - 1] < len(citations) - i + 1):
                    ans = len(citations) - i
                    break
                else:
                    ans=0
        return ans


var = Solution()
print(var.hIndex([11,15]))
