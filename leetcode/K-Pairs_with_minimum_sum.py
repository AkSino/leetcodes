#We will keep on pushing the array value to a min heap with values inside array as [sum value, i index, j index]
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        result = []
        minHeap = []

        if not nums1 or not nums2 or k <= 0:
            return result

        for i in range(len(nums1)):
            heapq.heappush(minHeap, [nums1[i] + nums2[0], i, 0])

        while minHeap and len(result) < k:
            _, i, j = heapq.heappop(minHeap)

            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(minHeap, [nums1[i] + nums2[j + 1], i, j + 1])
        return result

var=Solution()
print(var.kSmallestPairs([1,2,3,4],[3,4,5,6],6))