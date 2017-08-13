time = input().strip()
length=int(len(time))
last=time[length-2]+time[length-1]
second=(time[length-4]+time[length-3])
timeArray=time.split(":")
hour=((timeArray[0]))
min=(timeArray[1])

if (last=="PM") and (int(hour)!=12):
    hour=int(hour)+12
elif (last=="AM") and (int(hour)==12):
    hour="00"
else:
    pass

print(hour,":",min,":",second,sep="")
