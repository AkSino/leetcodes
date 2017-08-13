import sys


s = input().strip()
string=list(s)
n = int(input().strip())
def abc(string):
    result = []
    flag = 1
    dict = {}
    for i in range(ord("a"), ord("z") + 1):
        dict[chr(i)] = i - 96
    result.append(dict[string[len(string) - 1]])
    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            if (flag != 0):
                result.append(dict[string[i]])

            result.append((result[len(result) - 1] + dict[string[i]]))
            flag = 0
        if string[i] != string[i + 1]:
            flag = 1
            result.append(dict[string[i]])
    return result
pqr=[]
arar=abc(string)

pqr=set(arar)

for a0 in range(n):
    x = int(input().strip())

    if x in pqr:
        print("Yes")
    else:
        print("No")