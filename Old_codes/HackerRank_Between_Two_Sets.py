def getTotalX(a, b):
    arr=[]
    start=a[len(a)-1]
    end=b[len(b)-1]
    for i in range(start,end+1):
        if divided(b,i) and divide(a,i):
            arr.append(i)
    return len(arr)

def divided(lis,num):
    for i in lis:
        if (i%num)!=0:
            return False
    return True
def divide(lis,num):
    for i in lis:
        if(num%i)!=0:
            return False
    return True

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)

