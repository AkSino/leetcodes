import random
from collections import  defaultdict
a=[1,2]
weight=[1,1]
aux=[weight[0]]
for i in range(1,len(weight)):
    aux=aux+[weight[i]+aux[i-1]]

dict=defaultdict(int)
for _ in range(10054):
    rand = random.randint(1, aux[-1])
    for i in range(len(aux)):
        if aux[i]>rand:
            dict[a[i]]+=1
            break

print(dict)