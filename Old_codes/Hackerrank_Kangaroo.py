def kangaroo(x1, v1, x2, v2):
    x = 1
    while x < 5000:
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
        x+=1
    return "NO"
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

#Instead of using above method use formula
# x2-x1%v2-v1=0