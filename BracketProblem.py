def findIndex(patern, index):

    stack = []
    for i in range(len(patern)):
        if(i==index):
            stack.append("A")
            continue
        if(patern[i]=="("):
            stack.append("(")
        elif(patern[i]==")"):
            s=stack.pop(-1)
            if(s=="A"):
                return i

print(findIndex("((())())", 1))

import math
