class Solution(object):
    def findAnagrams(self, s, p):
        a=[0 for i in range(256)]
        for each in p:
            a[ord(each)]+=1
        indexes=[]
        flag=0
        for j in range(len(s)-len(p)+1):
            if j>0 and j<len(s)-len(p) and s[j+len(p)-1]==s[j-1] and flag==1:
                indexes.append(j)
                continue
            count=0
            b=list(a)
            for i in range(len(p)):
                if((i+j)<len(s)):
                    if b[ord(s[i+j])]>0:
                        b[ord(s[i+j])]-=1
                        count+=1

                    else:
                        flag=0
                        break
                    if count==len(p):
                        flag=1
                        indexes.append(j)
        return indexes

var=Solution()
print(var.findAnagrams("aba"))