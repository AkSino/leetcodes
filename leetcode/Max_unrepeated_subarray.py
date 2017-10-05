#We can use hash map with all the characters in it and initial value -1. As soon as we find it we update it with the index.

arr=['A','B','C','D','A']
i=0
a={}
max_len=0
max_len2=0
while i<len(arr):
    if arr[i] not in a:
        a[arr[i]]=i
        max_len+=1
        if i==len(arr)-1 and max_len>max_len2:
            max_len2=max_len
        i=i+1


    else:
        i=a[arr[i]]+1
        a.clear()
        if max_len>max_len2:
            max_len2=max_len
        max_len=0


print(max_len2)