def function(passwords):
    final_array=[]
    for j in range(len(passwords)):
        string=list(passwords[j])
        for i in range(len(string)):
            if string[i]=="s" or string[i]=="S":
                string[i]="5"
        if len(string)%2==1 and len(string)>2 and string[(len(string)//2)].isdigit():
            string[(len(string) // 2)]=str(int(string[(len(string)//2)])*2)
            string=list("".join(string))

        if len(string)%2==0:
            a=string[-1].islower()
            b=string[0].islower()
            string[0],string[-1]=string[-1],string[0]
            if a:
                string[0]=string[0].upper()
            else:
                string[0] = string[0].lower()
            if b:
                string[-1]=string[-1].upper()
            else:
                string[-1] = string[-1].lower()

        ind = 0
        match = "extcapital"
        lower = False
        upper = False
        ans = -1
        while ind < len(string):
            if ans < 0:
                if string[ind] == "N" or string[ind] == "n":
                    ind += 1
                    pick = 0
                    while pick < len(match) and ind < len(string):
                        if string[ind] == match[pick]:
                            lower = True
                            pick += 1
                            ind += 1
                            if pick == len(match) and (lower or upper):
                                ans = ind - pick - 1

                        elif string[ind] == match[pick].upper():
                            upper = True
                            pick += 1
                            ind += 1
                            if pick == len(match) and (lower or upper):
                                ans = ind - pick - 1
                        else:
                            lower = False
                            upper = False
                            break
                else:
                    ind += 1
            else:
                break

        if ans<0:
            final_array.append("".join(string))
        else:
            final_array.append("".join(string[0:ans])+"".join(reversed(string[ans:ans+4]))+"".join(string[ans+4:len(string)]))

    return final_array

for each in (function(["nextcapital","NeXtcapital","nExtCapitAli5cool","hooRayNexTcapItaLnextcapitall"])):
    print(each)













