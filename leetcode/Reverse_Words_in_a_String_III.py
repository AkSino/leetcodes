def reversed(str):
    result=""
    for i in range(len(str)-1,-1,-1):
        result=result+str[i]
    return result

inp_str="Let's take LeetCode contest"

converted_array=inp_str.split(" ")

for i in converted_array:
    print(reversed(i),end=" ")




