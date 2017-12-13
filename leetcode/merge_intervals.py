class Solution:
    def merge(self, intervals):
        i=1
        result=[]
        last=0
        for i in intervals:
            if i.start>intervals[i-1][1]:
                result.append([intervals[last][0], intervals[i - 1][1]])
                last=i
                i=i+1
            else:
                i=i+1
        result.append([intervals[last][0], intervals[i - 1][1]])
        return result

var=Solution()
print(var.merge([[1,3],[2,6],[8,10],[15,18]]))