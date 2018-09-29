class Solution(object):
    def merge(self, nums1, m, nums2, n):
        lastIndex = m + n - 1
        end1 = m - 1
        end2 = n - 1

        while (end1 >= 0 and end2 >= 0):
            if (nums1[end1] > nums2[end2]):
                nums1[lastIndex] = nums1[end1]
                end1 -= 1
                lastIndex -= 1
            else:
                nums1[lastIndex] = nums2[end2]
                end2 -= 1
                lastIndex -= 1

        if (end1 < 0):
            while (end2 >= 0):
                nums1[lastIndex] = nums2[end2]
                end2 -= 1
                lastIndex -= 1
        else:
            while (end1 >= 0):
                nums1[lastIndex] = nums1[end1]
                end1 -= 1
                lastIndex -= 1

var=Solution()
a=[1,2,3,0,0,0]
var.merge(a, 3, [2,5,6], 3)
print(a)

