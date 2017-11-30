string="544"
prev="a"
sumi=1
result=""
prev=string[0]
if(len(string))==1:
        result = result + str(sumi) + prev
else:
    for i in range(1,len(string)):

        if string[i]==string[i-1]:
            if(i==len(string)-1):
                sumi+=1
                result = result + str(sumi) + prev
            sumi+=1
        else:
            result=result+str(sumi)+prev
            prev=string[i]
            sumi=1
            if (i == len(string) - 1):
                result = result + str(sumi) + prev


print(result)

