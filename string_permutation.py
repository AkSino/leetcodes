def permutation(input_string,start,end):
    if start==end:
        print(input_string)
    else:
        for i in range(start,end+1):
            input_string[start],input_string[i]=input_string[i],input_string[start]
            permutation(input_string,start+1,end)
            input_string[start], input_string[i] = input_string[i], input_string[start] #It is used so that there miht be no change
                                                                                         #in the input_string and for every


#First A is swapped with A, and permutation run on B,C
#Second A is swapped with B , and permutation run on A,C
#Third A swapped with C, and permutation run on B,A

# And for all these three steps we have to firstly swap the number and then again come back to the original pattern so that we
# can swap the other pair of number easily

str="ABC"
lists=list(str)
start=0
end=len(lists)-1
permutation(lists,start,end)