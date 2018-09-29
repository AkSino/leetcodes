class Solution:
    def findPeakElement(self, nums):
        if(len(nums)==0):
            return
        elif(len(nums)==1):
            return 0
        return self.helperFunction(nums, 0, len(nums) - 1)

    def helperFunction(self, array, start, end):
        mid = (start + end) // 2

        if (mid == 0):
            if (array[mid + 1] < array[mid]):
                return 0
            else:
                return 1
        elif (mid == len(array) - 1):
            if (array[mid - 1] < array[mid]):
                return len(array) - 1
            else:
                return mid - 1

        if (array[mid + 1] < array[mid] > array[mid - 1]):
            return mid
        else:
            if (array[mid + 1] > array[mid]):
                return self.helperFunction(array, mid + 1, end)
            elif (array[mid - 1] > array[mid]):
                return self.helperFunction(array, start, mid - 1)

var=Solution()
print(var.findPeakElement([1,2,3,1]))