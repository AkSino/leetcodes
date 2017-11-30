container_walls=[2,2,5,2,3,7,4,8,9]
min_array=[]

maximum=0
index=0
for i in range(len(container_walls)-1):
    ans=min(container_walls[i],container_walls[i+1])
    min_array.append(ans)
    if maximum<ans:
        maximum=ans
        index=i




print(container_walls[i], container_walls[i+1])