#https://leetcode.com/problems/longest-valid-parentheses/discuss/

input_string="))((()))()())((()()()"
class Solution():
    def longestValidParentheses(self,input_string):
        stack=[]
        left=-1
        maxim=0
        if len(input_string)==0:
            return 0
        for i in range(len(input_string)):
            if input_string[i]=="(":
                stack.insert(0,i)
            else:
                if len(stack)==0:
                    left=i
                else:
                    stack.pop(0)
                    if(len(stack)==0):
                        maxim=max(maxim,i-left)
                    else:
                        maxim=max(maxim,i-stack[0])
        return maxim

