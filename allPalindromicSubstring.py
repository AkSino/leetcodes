a="wowpurerocks"
def  count_palindromes( S):
    if S=="":
        return 0
    if len(S)==1:
        return 1
    count=0
    mat=[[True for i in range(len(S))] for j in range(len(S))]

    for i in range(len(S)):
        mat[i][i]=True
        count+=1

    for length in range(1,len(S)+1):
        for i in range(0,len(S)-length):
            if S[i+length]==S[i]:
                mat[i][i+length]=mat[i+1][i+length-1]
                if mat[i][i+length]==True:
                    count+=1
            else:
                mat[i][i+length]=False

    print (count)

count_palindromes(a)
