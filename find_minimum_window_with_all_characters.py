string="abcccccmva"
pattern="ma"

pattern_arr=[0 for i in range(256)]
string_arr=[0 for i in range(256)]

for i in range(len(pattern)):
    pattern_arr[ord(pattern[i])]+=1
max_len=10000000000
count=0
start=0
for j in range(len(string)):
    string_arr[ord(string[j])]+=1
    if (pattern_arr[ord(string[j])]!=0 and pattern_arr[ord(string[j])]>=string_arr[ord(string[j])]):
        count+=1
    if count==len(pattern):

        while string_arr[ord(string[start])] > pattern_arr[ord(string[start])] or pattern_arr[ord(string[start])] == 0:
            if string_arr[ord(string[start])]>pattern_arr[ord(string[start])]:
                string_arr[ord(string[start])]-=1
            start+=1

        min_len=min(max_len,j-start+1)
print(min_len)