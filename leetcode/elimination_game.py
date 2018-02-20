class Solution(object):
    def lastRemaining(self, n):
        steps=1
        length=n
        odd=1
        first=1
        last=n
        while length>1:
            if length%2==0:
                steps*=2
                length=length/2
                first+=steps
