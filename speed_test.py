import time
start=time.time()
a=[10 for i in range(100000000)]

for each in range(len(a)):
    a[each]=100
end=time.time()

print(end-start)