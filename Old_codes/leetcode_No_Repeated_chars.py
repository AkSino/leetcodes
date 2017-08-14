string_test="pwwkew"
out_string=[]
longest_string=0
test_len=0
test_array=[]
for i in string_test:
    if i in out_string:
        if longest_string<test_len:
            longest_string=test_len
            test_len=0
            test_array=out_string
            out_string=[]
        else:
            test_len = 0
            out_string = []
    if i not in out_string:
        out_string.append(i)
        test_len+=1


print (test_array)



