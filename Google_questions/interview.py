import math

class Solution(object):
    def triangleNumber(self, str1,str2):
        len1=len(str1)
        len2=len(str2)

        repeat=math.ceil(len2/len1)

        ans=int(len2/len1)

        if len2==0 or len1==0:
            return -1
        elif str2 in repeat*str1:
            return repeat
        elif str2 in (repeat+1)*str1:
            return repeat+1
        else:
            return -1


var=Solution()

print(var.triangleNumber("abc","cabcab"))
