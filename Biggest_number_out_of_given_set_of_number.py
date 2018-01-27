import heapq
a=[1,2,3,4,99,89,567,64]
a.sort()
string=list(map(str,a))
length=len(string[-1])

def multiply_string(string):
    global length
    while len(string)<=length:
        string+=string
    return string[0:length]

final_ans=list(map(multiply_string,string))

heap=[]
for each in final_ans:



