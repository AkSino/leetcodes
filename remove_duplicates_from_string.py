def removeDuplicate(stri):
    hash={}
    for each in stri:
        hash[each]=1

    for each in stri:
        if hash[each]==1:
            print(each,end="")
            hash[each]-=1

removeDuplicate("VVVABVVVV")