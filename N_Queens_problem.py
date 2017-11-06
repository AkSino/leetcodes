matrixes=[[True for i in range(5)]for j in range(5)]



def markImpossibleElements(matrixes,x,y):
    matrixes[x][y]=False
    for i in range(len(matrixes)):
        for j in range(len(matrixes)):
            if i-x!=0 and j-y!=0:
                if (j-y)/(i-x)==1 or (j-y)/(i-x)==-1:
                    matrixes[i][j]=False
    i=0
    j=0
    while i<len(matrixes):
        matrixes[i][y]=False
        i+=1
    while j<len(matrixes):
        matrixes[x][j]=False
        j+=1
    return matrixes

def

print(markImpossibleElements(matrixes,0,2))