word="VARDANABMEN"

array=[None for i in range(256)]
count=0
maximum=0
for i in range(len(word)):
    if array[ord(word[i])]==None:
        array[ord(word[i])]=i
        count+=1
    elif i-array[ord(word[i])]>count:
        count+=1
        array[ord(word[i])]=i
    elif i-array[ord(word[i])]<=count:
        count=i-array[ord(word[i])]
        array[ord(word[i])] = i
    maximum = max(maximum, count)

print(maximum)