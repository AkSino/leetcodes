class Solution():
    def longestPalindromeSubseq(self, s):
        array=[[0 for i in range(len(s))] for j in range(len(s))]

        for i in range(len(array)):
            array[i][i]=1
        for i in range(1,len(array)):
            for j in range(0,len(array)-i):
                if s[j]==s[j+i]:
                    array[j][j+i]=array[j+1][j+i-1]+2
                else:
                    array[j][j+i]=max(array[j+1][j+i],array[j][j+i-1])
        return array[0][len(array)-1]





# class Solution():
#     def helper(self,longest,s):
#         if len(s)==1:
#             return 1
#         elif len(s)==0:
#             return 0
#         else:
#             if s[0]==s[-1]:
#                 return max(longest,2+self.helper(longest,s[1:-1]))
#             else:
#                 a=max(self.helper(longest,s[1:]),self.helper(longest,s[:-1]))
#                 return max(a,longest)
#     def longestPalindromeSubseq(self, s):
#         longest=-109
#         return (self.helper(longest,s))


var=Solution()
print(var.longestPalindromeSubseq("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"))