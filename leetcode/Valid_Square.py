#https://leetcode.com/problems/valid-square/description/
import math

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        if (p1==p2 or p1==p3 or p1==p4 or p2==p3 or p2==p4 or p3==p4):
            return False
        p12=self.findDistance(p1,p2)
        p13=self.findDistance(p1,p3)
        p14=self.findDistance(p1,p4)


        if(p12==p13 and self.findDistance(p2,p4)==self.findDistance(p3,p4)):
            if (p14> math.sqrt(2) * p12 - 0.00001 and p14 < math.sqrt(2) * p12 + 0.00001) and (self.findDistance(p2,p3)>math.sqrt(2)*p12-0.00001 and self.findDistance(p3,p2)<math.sqrt(2)*p12+0.00001):
                return True
        if(p12==p14):
            if (p13 > math.sqrt(2) * p12 - 0.001 and p13 < math.sqrt(2) * p12 + 0.001) and (self.findDistance(p2,p4)>math.sqrt(2)*p12-0.001 and self.findDistance(p2,p4)<math.sqrt(2)*p12+0.001):
                return True
        if (p13==p14):
            a=math.sqrt(2)*p13
            if (p12>math.sqrt(2)*p13-0.001 and p12<math.sqrt(2)*p13+0.001) and (self.findDistance(p3,p4)>math.sqrt(2)*p13-0.001 and self.findDistance(p3,p4)<math.sqrt(2)*p13+0.001):
                return True
        return False

    def findDistance(self,p,q):
        return math.sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2))

p1 = [1,1]
p2 = [0,1]
p3 = [1,2]
p4 = [0,0]

var=Solution()
print(var.validSquare(p1,p2,p3,p4))