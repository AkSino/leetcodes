def super_reduced_string(s):
    arra=list(s)
    parra=[]
    carra=list(arra)
    flag=2
    make=1
    while flag>1:
        parra = []
        flag=0
        arra=list(carra)
        for i in range(len(arra)):
            if make == 2:
                make = 1
                continue
            if i==len(arra)-1:
                parra.append(arra[i])
            else:
                if arra[i]!=arra[i+1]:
                    parra.append(arra[i])
                if arra[i]==arra[i+1]:
                    flag=2
                    make=2
            carra=list(parra)
    if arra:
        return ''.join(arra)
    if not arra:
        return "Empty String"

s = input().strip()
result = super_reduced_string(s)
print(result)