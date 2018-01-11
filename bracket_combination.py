def put_bracket(num):
    a=set()

    if num==1:
        return ["()"]
    else:
        for each in put_bracket(num-1):
            a.add("()"+each)
            a.add("(" + each +")")
            a.add(each+"()")
    return list(a)
print(put_bracket(2))