denominations=[2,3]
balance=7
input_array=[[0 for p in range(balance+1)] for q in range((len(denominations)+1))]
input_array[0][0]=0
for i in range(1,len(denominations)+1):
    for j in range(1,balance+1):
        if j<denominations[i-1]:
            input_array[i][j]=input_array[i-1][j]
        elif j%denominations[i-1]==0:
            input_array[i][j]=int(j/denominations[i-1])
        else:
            if input_array[i][j - denominations[i-1]]==0 or (j - denominations[i-1]<0):
                input_array[i][j] = input_array[i - 1][j]
            else:
                input_array[i][j]=input_array[i][j-denominations[i-1]]+1
if input_array[len(denominations)][balance]==0:
    print("Nikal")
ver=len(input_array)-1
hor=len(input_array[0])-1
answer=[]
while ver>0 and hor>0:
    if hor-denominations[ver-1]<0:
        ver-=1
    if input_array[ver][hor-denominations[ver-1]]==input_array[ver][hor]-1:
        # if hor-denominations[ver-1]==0:
        answer.append(denominations[ver-1])
        hor-=denominations[ver-1]

    else:
        ver-=1
print(input_array)
print(answer)