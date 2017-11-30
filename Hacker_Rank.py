n,m= map(int,input().split(' '))
printer_value = list(map(int, input().strip().split(' ')))
papers_value = list(map(int, input().strip().split(' ')))
printer_value.sort()
middle_arr=[0 for x in range(len(printer_value))]

for i in range(len(printer_value)):
    ans=0
    for j in range(len(papers_value)):
        if papers_value[j]<=printer_value[i]:
            ans+=1
    middle_arr[i]=ans
max_div=-(-middle_arr[-1]//n)
to_sub=0
tan=[]
for i in range(n-1):
    middle_arr[i]=middle_arr[i]-to_sub
    if middle_arr[i]/max_div>=1:
        to_sub=to_sub+max_div
        n=n-1
        tan.append(max_div)
        middle_arr[-1]=middle_arr[-1]-max_div
        max_div = -(-(middle_arr[-1] ) // n)



    else:
        to_sub=to_sub+middle_arr[i]
        n=n-1
        tan.append(middle_arr[i])
        middle_arr[-1] = middle_arr[-1] - middle_arr[i]
        max_div = -(-(middle_arr[-1] ) // n)

tan.append(middle_arr[-1])

print(max(tan))
