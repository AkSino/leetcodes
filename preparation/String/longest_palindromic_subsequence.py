def find_subsequence(string):
    if string=="":
        return 0
    elif len(string)==1:
        return 1
    else:
        if string[0]==string[len(string)-1]:
            ans=2+find_subsequence(string[1:len(string)-1])
        else:
            ans=max(find_subsequence(string[0:len(string)-1]),find_subsequence(string[1:len(string)]))
    return ans


print(find_subsequence("VAAFAAV"))