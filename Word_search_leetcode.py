#https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board, word):
        visited=[[False for i in range(len(board[0]))] for j in range(len(board))]
        index=0
        character=word[index]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==character:
                    visited[i][j]=True
                    if self.helper(board,index+1,i,j,word,visited):
                        return True
                    visited[i][j]=False
        return False

    def helper(self,board,index,i,j,word,visited):
        if index==len(word):
            return True
        else:
            x=[0,-1,0,1]
            y=[1,0,-1,0]
            for m in range(len(x)):
                p=i+x[m]
                q=j+y[m]
                if(0<=p<len(board) and 0<=q<len(board[0]) and board[p][q]==word[index] and visited[p][q]==False):
                    visited[p][q] = True
                    if self.helper(board, index + 1, p, q, word,visited):
                        return True
                    visited[p][q] = False
            return False

board=[
    ["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]
]
word = "ABCESEEEFS"
vard=Solution()
print(vard.exist(board,word))