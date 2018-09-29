class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        definedPat=self.findPattern(pattern)
        output=[]
        for each in words:
            if(self.findPattern(each) == definedPat):
                output.append(each)
        return output
    def findPattern(self, word):
        dict={}
        counter=0
        pattern=""
        for each in word:
            if each in dict:
                pattern+=str(dict[each])
            else:
                counter+=1
                dict[each]=counter
                pattern+=str(dict[each])
        return pattern


var=Solution()
print(var.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
