class Solution:
    def searchMatrix(self, matrix, target):
        i=0
        j=0
        if len(matrix)==0:
            return False
        if len(matrix[0])==0:
            return False

        while 0<=i<len(matrix) and 0<=j<len(matrix[0]):
            if target>matrix[i][-1]:
                i+=1
                continue
            elif matrix[i][0]<=target<=matrix[i][-1]:
                return self.search_array(matrix[i],target,0,len(matrix[i]))
            i+=1
        return False
    def search_array(self,array,target,start,end):
        mid=(start+end)//2
        if array[mid]==target:
            return True
        if start==end and array[start]!=target:
            return False
        if target>array[mid]:
            return self.search_array(array,target,mid+1,end)
        elif target<array[mid]:
            return self.search_array(array,target,start,end-1)

var=Solution()
print(var.searchMatrix([[1]],0))