minim = -100000
def RodCutting(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0
    maintain_len=[[] for x in range(n+1)]
    maintain_len[0]=[0]
    length_arr=len(price)
    max_val = minim
    for i in range(1, n + 1):
        j=0
        while j<length_arr and i-j-1>=0:
            if max_val<(price[j] + val[i - j - 1]):
                max_val=(price[j] + val[i - j - 1])
                if (i-j-1)!=0:
                    maintain_len[i]=[j+1]+maintain_len[i-j-1]
                else:
                    maintain_len[i] = [j + 1]
            j=j+1
        val[i] = max_val
    return val[n],maintain_len[n]
arr = [2,6,10,2]
size = len(arr)
print("Maximum Value is " + str(RodCutting(arr, 5)[0]))
print("Number of cuts " + str(RodCutting(arr, 5)[1]))