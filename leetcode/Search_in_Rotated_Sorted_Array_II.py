class Solution:
    def binarySearch(self,array,target,start,end):
        if start==end:
            if array[start]!=target:
                return False
        mid=(start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]>target:
            return self.binarySearch(array,target,start,mid-1)
        elif array[mid]<target:
            return self.binarySearch(array,target,mid+1,end)

    def findMid(self,array,target,start,end):
        mid=(start+end)//2
        if array[mid]<array[mid-1] and array[mid]<array[mid+1]:
            return mid
        elif array[mid]>array[-1]:
            return self.findMid(array,target,mid+1,end)
        elif array[mid]<array[-1]:
            return self.findMid(array,target,start,mid-1)



    def search(self, nums, target):
        if nums[0]<nums[-1]:
            return self.binarySearch(nums,target,0,len(nums))
        else:
            array=1


var=Solution()
print(var.findMid([9,8,7,6,5,1,2,3],4,0,7))

