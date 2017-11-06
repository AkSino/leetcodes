beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

def WordLadder(begin,end,wordList):
    jf


def MatchLetter(word1,word2):
    diff=0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            diff+=1
    if diff==1:
        return True
    else:
        return False