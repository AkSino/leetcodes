class Solution:
    def grayCode(self, n):
        first=n*"0"
        mapping={}
        mapping[first]=True

        ans=[]
        ans.append(self.binToDecimal(first))
        for i in range(2**n - 1):
            for i in range(len(first)-1, -1, -1):
                mid=self.flip(first, i)
                if(mid not in mapping):
                    mapping[mid]=True
                    ans.append(self.binToDecimal(mid))
                    first=mid
                    break
                else:
                    mid=self.flip(first, i)
        return ans

    def flip(self, string, bit):
        string=list(string)
        if(string[bit]=="1"):
            string[bit]="0"
        else:
            string[bit]="1"

        return "".join(string)

    def binToDecimal(self, string):
        sum=0
        for i in range(len(string)-1, -1, -1):
            sum=sum+int(string[i])*(2**(len(string)-i-1))
        return sum

var=Solution()
print(var.grayCode(0))