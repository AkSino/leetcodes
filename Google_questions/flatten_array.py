# [[1,1],2,[1,1]]
import nltk
class Solution():
    def __init__(self):
        self.result=[]
    def flatenArray(self,arr):

        for each in arr:
            if type(each)==int:
                self.result.append(each)
            else:
                self.flatenArray(each)
        return (self.result)

S=Solution()
print(S.flatenArray([1,[4,[6]]]))




