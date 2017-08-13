arra,slit=input().strip().split(' ')
arra,slit=[int(arra),int(slit)]
my_list=list(map(int, input().strip().split(' ')))
master=[]
m=0
noti=0
def median(arra):
    p=list(arra)
    p.sort()
    if len(p)%2==0:
        mid=int(len(p)/2)
        medians=((p[mid-1]+p[mid])/2)
    else:
        pi = int(len(p) / 2)
        medians= p[pi]
    return medians

for j in range(0,slit):
    master.append(my_list[j])
for i in range (slit,len(my_list)-1):
    if i==slit:
        result = median(master)
        if my_list[i] >= 2 * result:
            noti += 1
        continue
    master.pop(0)
    master.append(i)
    result=median(master)
    if my_list[i]>=2*result:
        noti+=1

print(noti)
