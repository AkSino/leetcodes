from math import ceil
number=str(12345)
mid=int(ceil(len(number)/2))
ans=int(number[:mid])
rem_ans=int(number[mid:len(number)])
cand=[]

if (len(ans)>len(rem_ans)):
    for i in [ans-1,ans,ans+1]:







