def func1(var,num):
    if num==0:
        return
    var.append(1)
    func1(var,num-1)
    return var

print(func1([],5))