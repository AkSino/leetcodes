ans=[1,2,2]
cur="1"
count=0
for each in ans:
    count+=1
    if count>=3:

        if each==1:
            ans.append(int(cur))
        else:
            ans.append(int(cur))
            ans.append(int(cur))

        if cur=="1":
            cur="2"
        else:
            cur="1"
    if len(ans)==30:
        break

print(ans)