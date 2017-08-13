data="saveChangesInTheEditor"
arra=list(data)
count=1
for (i) in range(len(arra)):
    if i==1:
        continue
    else:
        if str(arra[i]).isupper():
            count+=1

print(count)
