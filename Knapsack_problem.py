def Knapsack(val,wt,W):
    if W<=0:
        return 0
    maxim=0
    for i in range(len(wt)):
        if wt[i]>W:
            continue
        else:
            maxim=max(maxim,val[i]+Knapsack(val,wt,W-wt[i]))
    return maxim


val = [600, 100, 900]
wt = [9, 5, 45]
W = 50

print(Knapsack(val,wt,W))