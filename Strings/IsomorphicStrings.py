class Solution:
    def isIsomorphic(self, s, t):

        dict={}
        dict2={}

        for i in range(len(s)):
            if (s[i] not in dict):
                if(t[i] in dict2):
                    return False
                dict[s[i]]=t[i]
                dict2[t[i]] = s[i]
            else:
                if(dict[s[i]] != t[i]):
                    return False
        return True

var=Solution()
print(var.isIsomorphic("ab", "ca"))