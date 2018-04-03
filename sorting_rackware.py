import datetime
a=['f','r','t','o']
b=[]
for i in range(len(a)):
    b.append(ord(a[i]))

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if b[i]>b[j]:
            b[i],b[j]=b[j],b[i]


with open() as file:
    file
def merge(arr1,arr2):
    arr=[]
    i=0

    while i<len(len(arr1)) and j<len(arr2):
        if arr1[i]>arr2[i]:
            arr.append(arr1[i])
        else:
            arr.append(arr2[i])
    return arr

def mergeSort(starting,end,array):
    if starting==end:
        merge()
    mid=(starting+end)//2

for i in range(len(a)):
    a[i]=a[i]+str(datetime.date.today())

print(a)