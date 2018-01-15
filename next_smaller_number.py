class Solution():
    def nextSmaller(self,num):
        num=list(str(num))
        for i in range(len(num)-2,-1,-1):
            if num[i+1]>num[i] and i ==0:
                return False
            else:
                if num[i+1]<num[i]:
                    br_point=i
                    break
        num=num[0:br_point+1]+sorted(num[br_point+1:len(num)],reverse=True)

        for i in range(br_point,len(num)):
            if num[i]<num[br_point]:
                num[i],num[br_point]=num[br_point],num[i]
                break
        return num

var=Solution()
print(var.nextSmaller(6534))
