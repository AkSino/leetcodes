class Solution(object):
    def minDistance(self, word1, word2):
        dynamic=[[i for i in range(len(word1)+1)] for j in range(len(word2)+1)]

        if(len(word1)==0):
            return len(word2)
        if(len(word2)==0):
            return len(word1)

        for i in range(0, len(dynamic)):
            for j in range(0, len(dynamic[0])):
                if(i==0 or j==0):
                    dynamic[i][j]=i+j
                else:
                    if(word1[j-1] == word2[i-1]):
                        dynamic[i][j]=dynamic[i-1][j-1]
                    else:
                        dynamic[i][j]=min(dynamic[i-1][j-1], dynamic[i][j-1], dynamic[i-1][j]) + 1
        return dynamic[len(word2)][len(word1)]

var=Solution()
print(var.minDistance("sea", "ate"))