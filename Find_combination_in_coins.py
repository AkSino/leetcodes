amount=10
coins=[1,2,5]
number_of_coins=len(coins)
dict={}
arr=[[] for x in range(amount+1)]
arr[0]=[]

for i in coins:
    for j in range(1,amount+1):
        if i==j:
            arr[j].append([j])
        if i<j:
            diff=j-i
            for ph in arr[diff]:
                arr[j].append(ph+[i])

print(arr[amount])