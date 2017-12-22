class Solution:
    def simplifyPath(self, path):
        stack=[]
        fin=""
        ans=path.split(sep="/")
        for each in ans:
            if each=="" or each==".":
                continue
            if each==".." and len(stack)!=0:
                stack.pop(0)
            if each != '..' and each != "":
                stack.insert(0,each)
        if len(stack)==0:
            return "/"
        for i in range(len(stack)-1,-1,-1):
            fin=fin+"/"+stack[i]
        return fin
vardan=Solution()
print(vardan.simplifyPath("/.."))
