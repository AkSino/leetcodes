inputs="*******"
array=list(inputs)
ans=0
def modify_array(array,indexi,effect,visited,record):
    if indexi-2<0 or visited[indexi]==True:
        return
    else:
        visited[indexi]=True
        if array[indexi-2]=="*":
            modify_array(array,indexi-2,effect*2,visited,record)
        else:
            record[indexi-2]=effect
    return record
record=[1 for x in range(len(array))]
visited=[False for p in range(len(array))]
for i in range(len(array)-1,-1,-1):
    if array[i]=="*":
        modify_array(array,i,2,visited,record)
    else:
        continue
for i in range(len(array)):
    if array[i]=="<":
        ans=ans-(record[i])
    elif array[i]==">":
        ans = ans + (record[i] * 1)
    else:
        continue
print(ans)


