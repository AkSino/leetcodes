import time
num=1
den=97
graph={}
def calculate(num,den):
    count=0
    while True:
        count+=1
        rem=num%den
        if rem in graph:

            return (len(graph),count)
        elif rem==0:
            return 0,count
        else:
            graph[rem]=1
            num=rem*10
maxim=0
start=time.time()
steps=0
for i in range(1,10000):
    for j in range(1,10000):
        maxim=max(maxim,calculate(i,j)[0])
        steps=steps+calculate(i,j)[1]
end=time.time()
print(steps)
print(maxim)
print(end-start)