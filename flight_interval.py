a=[900,902,904,906,908,910]
b=[902,904,906,908,910,912]
b.sort()

i=0
j=1
term=1
while(j<len(a)):
    if a[j]<b[i]:
        temp = j - i +1
        j+=1
        term=max(term,temp)

    elif a[j]==b[i]:
        j += 1
        temp = j - i
        term=max(term,temp)
        i+=1
    else:
        i=i+1
        j=j+1

print(term)


