#https://www.hackerrank.com/challenges/the-indian-job/problem

#b=int(input())
for i in range(1):
    # a=list(map(int,input().strip().split()))
    # b=list(map(int,input().strip().split()))
    strin1="4 136"
    strin2="51 97 22 92"

    a=list(map(int,strin1.strip().split()))
    b=list(map(int,strin2.strip().split()))
    guard=[0 for j in range(a[1])]
    b.sort(reverse=True)
    pointer=0
    final_ans=True
    for thief in range(len(b)):
        semi_guard=list(guard)
        if pointer+b[thief]<=len(guard):
            flag=False
            for index in range(pointer,pointer+b[thief]):
                semi_guard[index]+=1
                pointer+=1
                if semi_guard[index]>2:
                    flag=True
            if flag==True:
                semi_guard = list(guard)
                pointer=0
                for elem in range(thief):
                    semi_guard+=1
                    pointer+=1
                    if semi_guard[index] > 2:
                        final_ans=False
        elif b[thief]>len(guard):
            final_ans=False
        else:
            pointer=0
            semi_guard = list(guard)
            for elem in range(thief):
                semi_guard[elem] += 1
                pointer += 1
                if semi_guard[elem] > 2:
                    final_ans = False

print(final_ans)

