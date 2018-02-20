string="ab"
prefix="a"
suffix="b"


def prefixs(string1,string2):
    count=0
    j=len(string2)-1
    for i in range(len(string1)-1,-1,-1):
        if 0<=j<len(string2):
            if string1[i]==string2[j]:
                count+=1
                j-=1
            else:
                j=len(string2)-1
                count=0
    return count

def suffixs(string1,string2):
    count=0
    j=0
    for i in range(len(string1)):
        if 0 <= j < len(string2):
            if string1[i]==string2[j]:
                count+=1
                j+=1
            else:
                j=0
                count=0
    return count

print(suffixs(string,suffix)+prefixs(string,prefix))