import math
a=list(map(float,input().strip().split()))
for i in range(len(a)):
    a[i]=round(a[i],2)

if len(a)<=1:
    print("%.2f" % 0)
else:
    totlSum=sum(a)
    mean=round(totlSum/len(a),4)
    standDev=0
    for i in range(len(a)):
        standDev+=(a[i]-mean)**2
    print("%.2f" % math.sqrt(standDev/(len(a)-1)))
