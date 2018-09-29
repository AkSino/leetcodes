class Solution(object):
    def findRadius(self, houses, heaters):
        minRad=heaters[0] - houses[0]
        covered=heaters[0] + minRad

        if(len(heaters)==1):
            return max(minRad,  houses[-1] - heaters[0] )

        for i in range(1, len(heaters)):
            mid=(heaters[i] - heaters[i-1])//2
            covered=heaters[i] + mid
            if(covered>=len(houses)):
                minRad=max(minRad, houses[-1]-heaters[i-1])
                break
            else:
                minRad = max(minRad, mid)

        return minRad

var=Solution()
print(var.findRadius([1,2,3,4], [1, 4]))