#http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/
from nltk import EarleyChartParser

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, dict):
        if s == '':
            return True
        checklist = [False] * (len(s) + 1)
        checklist[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j + 1] in dict and checklist[j + 1] == True:
                    checklist[i] = True
        return checklist[0]
dict=["eecodee","eeleetee","eevee","nnu"]
var=Solution()
print(var.wordBreak("eecodeeeeveeeeleetee",dict))

a=[1]
