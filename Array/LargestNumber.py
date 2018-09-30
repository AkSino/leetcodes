class Solution(object):
    def largestNumber(self, nums):
        array = [0 for i in range(10)]
        ans = ""

        for each in nums:
            if (each == 0):
                array[each] += 1
            while each != 0:
                array[each % 10] += 1
                each = each // 10

        for i in range(len(array) - 1, -1, -1):
            ans += str(i) * array[i]
        return ans


var = Solution()
print(var.largestNumber([3, 30, 34, 5, 9]))
