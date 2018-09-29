class Solution(object):
    def smallestRangeI(self, A, K):
        if len(A)<=1:
            return 0
        else:
            mini=min(A)
            maxi=max(A)
        avg=(mini+maxi)//2

        if(mini+K>=avg):
            mini=avg
        else:
            mini=mini+K

        if(maxi-K<=avg):
            maxi=avg
        else:
            maxi=maxi-K
        return maxi-mini

var=Solution()
print(var.smallestRangeI([3,1,10], 4))