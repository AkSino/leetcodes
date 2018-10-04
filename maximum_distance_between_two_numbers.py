class Solution():
    def maximumGap(self,array):
        if (len(array)==1):
            return 0
        maxArray=[None for i in range(len(array))]
        minArray=[None for j in range(len(array))]
        minArray[0]=array[0]
        for i in range(1,len(array)):
            minArray[i]=min(array[i],minArray[i-1])

        maxArray[-1]=array[-1]
        for j in range(len(array)-2,-1,-1):
            maxArray[j]=max(array[j],maxArray[j+1])
        i=0
        j=0
        ans=-1
        while i<len(array) and j<len(array):
            if minArray[i]<=maxArray[j]:
                ans=max(ans,j-i)
                j+=1
            else:
                i+=1
        return ans
var=Solution()
print(var.maximumGap([2, 3, 10, 2, 4, 8, 1]))





