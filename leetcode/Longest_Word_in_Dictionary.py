words = ["a",  "app", "appl", "ap", "apply", "apple","baa","b","ba","ban","bana","banan"]
words.sort()
hashset=set()
for i in range(len(words)):
    if len(words[i])==1:
        hashset.add(words[i])
    else:
        if words[i][:-1] in hashset:
            hashset.add(words[i])


hashset=sorted(hashset)
ans=list(map(lambda x: len(x),hashset))
answer=max(ans)

for i in range(len(ans)):
    if ans[i]==answer:
        print(hashset[i])
        break

