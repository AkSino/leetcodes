class Solution:
    def partitionDisjoint(self, A):
        mini=-10000000000
        leftArray=[-1 for i in range(len(A))]
        rightArray = [-1 for i in range(len(A))]

        for i in range(len(A)):
            mini=max(mini, A[i])
            leftArray[i]=mini

        mini = 10000000000
        for i in range(len(A)-1, -1, -1):
            mini=min(mini, A[i])
            rightArray[i]=mini


        for i in range(1, len(A)):
            if(leftArray[i-1]<=rightArray[i]):
                return i

var=Solution()
print(var.partitionDisjoint([1,1,1,0,6,12]))