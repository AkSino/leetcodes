#https://leetcode.com/problems/monotone-increasing-digits/description/

class Solution:
    def monotoneIncreasingDigits(self, N):
        N=str(N)
        if len(N)==1:return N
        else:
            b=0
            c=1
            for i in range(1,len(N)):
                if int(N[i])>=int(N[i-1]):
                    c+=1
                if int(N[i])>int(N[i-1]):
                    b=i
                if int(N[i])<int(N[i-1]):
                    break
            if c==len(N):
                return int(N)
            else:
                return int(N[0:b]+(str(int(N[b])-1))+(len(N)-b-1)*"9")

var=Solution()
print(var.monotoneIncreasingDigits(989994))