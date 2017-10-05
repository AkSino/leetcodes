pattern=[1,2,3]
string=[1,4,3,2,6,2,3,1,2,3,5,6]

str_len=len(string)
pat_len=len(pattern)-1

i=0  #pointer for string
j=0  #pointer for pattern
while i<str_len:
    cur_str=string[i]
    cur_pat=pattern[j]
    if j==pat_len+1:
        print(i-pat_len)
    if cur_str==cur_pat:
        i=i+1
        j=j+1
        if j == pat_len + 1:
            j=0
            print(i - pat_len)
    if cur_str!=cur_pat:
        i=i+1
        j=j=0
