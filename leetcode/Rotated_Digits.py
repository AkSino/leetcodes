#https://leetcode.com/problems/rotated-digits/description/

class Solution:
    def rotatedDigits(self, N):
        if N==1:
            return 0
        good=["2","5","6","9"]
        falses=["3","4","7"]
        fake=["0","1","8"]
        flag=False
        count=0
        for i in range(1,N+1):
            wordFlag=False
            data=str(i)
            for char in data:
                if char in falses:
                    flag=False
                    break
                elif char in good:
                    wordFlag=True
                    flag=True
            if flag and wordFlag:
                count+=1
        return count

var=Solution()
print(var.rotatedDigits(857))