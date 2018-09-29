class Solution(object):
    def snakesAndLadders(self, board):
        return self.helperFunction(board, [len(board)-1, 0], 0)

    def helperFunction(self, board, start, stepCount):

        for i in range(1,7):



    def calculateIndex(self, board, index, step):
        while(step>=0):
            if((len(board)-1-index[0])%2==0):
                if(index[1]+1>len(board[0])):
                    index[1]=len(board[0]-1)
                    index[0]=index[0]-1
                    step-=1
                else:
                    index[1]=index[1]+1
                    step-=1
            if((len(board)-1-index[0])%2==1):
                if(index[1]-1<0):
                    index[1]=0
                    index[0]=index[0]-1
                    step-=1
                else:
                    index[1]=index[1]-1
                    step-=1
            if(index[0]==0 and index[1]==0):
                return [0,0]


