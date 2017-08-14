def rowDec(arra):
    row=arra[0]-1
    col=arra[1]
    arra=[row,col]
    return arra
def colDec(arra):
    row = arra[0]
    col = arra[1]- 1
    arra = [row, col]
    return arra
def rowInc(arra):
    row = arra[0] +1
    col = arra[1]
    arra = [row, col]
    return arra
def colInc(arra):
    row = arra[0]
    col = arra[1] +1
    arra = [row, col]
    return arra

n=4
arra=[4,4]

row=[rowDec(arra),rowInc(arra)]
col=[colDec(arra),colInc(arra)]
ping=[]

for i in range(2):
    pass
while arra[0]>0:
    arra=rowDec(arra)
    ping.append(arra)
print(ping)
