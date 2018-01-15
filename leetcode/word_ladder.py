#https://leetcode.com/problems/word-ladder/description/

class Solution:
    def ladderLength(self, beginWord, endWord, wordList,arraylist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        for i in range(len(wordList)):
            if self.match_word(beginWord,endWord):
                return arraylist+[beginWord]+[endWord]
            elif self.match_word(beginWord,wordList[i]):
                return self.ladderLength(wordList[i], endWord, wordList[0:i] + wordList[i + 1:len(wordList)], arraylist+[beginWord])
        return False


    def match_word(self,word1,word2):
        cut=0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                cut+=1
        if cut==1:
            return True
        else:
            return False

var=Solution()
print(var.ladderLength("hit","cog",["hot","dog","lot","log","cog","dot"],[]))