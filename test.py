my_list=list(map(int, input().strip().split(' ')))
master=[]
for j in range(0,len(my_list)):
    master.append(my_list[j])

master.sort()
print(master)