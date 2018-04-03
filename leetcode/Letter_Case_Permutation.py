#https://leetcode.com/problems/letter-case-permutation/description/


class Solution:
    def letterCasePermutation(self, S):
        if S=="":
            return [""]
        return self.helper(0,S,[])
    def helper(self,index,S,array):
        if index==len(S):
            return
        if S[index].isdigit():
            if index==len(S)-1:
                array.append(S)
            else:
                self.helper(index + 1, S, array)
        else:
            if index==len(S)-1:
                array.append(S[0:index] + self.reverseCase(S[index], 1) + S[index + 1:len(S)])
                array.append(S[0:index] + self.reverseCase(S[index], 0) + S[index + 1:len(S)])
            for i in range(2):
                self.helper(index+1,S[0:index] + self.reverseCase(S[index], i) + S[index + 1:len(S)],array)
        return array

    def reverseCase(self,char,status):
        if status:
            return char.upper()
        else:
            return char.lower()

var=Solution()
print(var.letterCasePermutation("a1b2"))

# if status==1 and index==len(S)-1:
#     array.append(S[0:index]+self.reverseCase(S[index],1)+S[index+1:len(S)])
#     return
# else:
#     if status==0:
#         self.helper(index, status + 1, S, array)
#         array.append(S[0:index] + self.reverseCase(S[index],0) + S[index + 1:len(S)])
#     else:
#         self.helper(index + 1, status - 1, S, array)
#         array.append(S[0:index] + self.reverseCase(S[index],1) + S[index + 1:len(S)])