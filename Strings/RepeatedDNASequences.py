from collections import defaultdict

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if(len(s)<10):
            return []
        ans=[]
        a=defaultdict(int)
        for i in range(len(s) - 9):
            a[s[i:i+10]]+=1
            if(a[s[i:i+10]]==2):
                ans.append(s[i:i+10])
        return ans

var=Solution()
print(var.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
