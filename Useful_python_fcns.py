#Interactive way to create  a array(list)
#URL for description is http://www.secnetix.de/olli/Python/list_comprehensions.hawk

S = [x**2 for x in range(10)]
m=3
n=4
table2=[0 for x in range(m)]
table = [[0 for x in range(m)] for x in range(n+1)]
print(table)
print(table2)

for i in range(m):
    table[0][i] = 1
print(table)

#Interactive use of if loop saving lots of coding:
x = table[i - S[j]][j] if i-S[j] >= 0 else 0