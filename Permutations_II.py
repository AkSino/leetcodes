var = []
def permutation(input_string,start,end):
    if start==end:
        var.append(''.join(input_string))


    else:
        for i in range(start,end+1):
            input_string[start],input_string[i]=input_string[i],input_string[start]
            permutation(input_string,start+1,end)
            input_string[start], input_string[i] = input_string[i], input_string[start] #It is used so that there miht be no change
                                                                                         #in the input_string and for every

    return var