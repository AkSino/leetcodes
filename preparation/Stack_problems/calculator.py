input_string="( + 7 ( * 8 12 ) ( * 2 ( + 9 4 ) 7 ) 3 )"
input_string=input_string.split()
stack=[]
def method(oper,elem1,elem2):
    elem1=int(elem1)
    elem2=int(elem2)
    if oper=="*":
        return elem1*elem2
    if oper=="+":
        return elem1+elem2
    if oper=="-":
        return elem1-elem2
    if oper=="/":
        return elem1/elem2
i=len(input_string)-1
while i>=0:
    if input_string[i]=="(":
        ans=stack.pop()
        stack.pop()
        stack.append(ans)
        i-=1
    elif input_string[i]=="*" or input_string[i]=="+" or input_string[i]=="/" or input_string[i]=="-":
        oper=input_string[i]
        elem1=stack.pop()
        elem2=stack.pop()
        if elem2==")":
            stack.append(")")
            stack.append(elem1)
            i-=1
        else:
            ans = method(oper, elem1, elem2)
            stack.append(ans)
    else:
        stack.append(input_string[i])
        i-=1

print(stack)



