#So basically id the middle element is even then the last element should be equal to current mid element
#If middle element is odd then

class Solution(object):
    def singleNonDuplicate(self, list):
        low, high = 0 , len(list)-1
        while (low<high):
            mid = low + int((high-low)/2)
            if (list[mid]!=list[mid+1] and list[mid]!=list[mid-1]):
                return list[mid]
            elif (mid%2 ==1 and list[mid]==list[mid-1]):
                low = mid+1
            elif (mid%2 ==0 and list[mid]==list[mid+1]):
                low = mid+1
            else:
                high = mid-1
        return list[high]

var=Solution()
print(var.singleNonDuplicate([5,1,1,2,2,3,3,4,4]))