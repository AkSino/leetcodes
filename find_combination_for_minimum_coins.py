def count(S, m, n):
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [10000 for k in range(n + 1)]

    # Base case (If given value is 0)
    table[0] = 0

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(S[i], n + 1):
            if j-S[i]==0:
                table[j]=1
            else:
                table[j] = min(table[j],table[j - S[i]]+1)

    return table[n]


# Driver program to test above function
arr = [1,15,25]
arr=sorted(arr)
m = len(arr)
n = 30
x = count(arr, m, n)
print(x)