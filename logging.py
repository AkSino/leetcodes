def function(x):
    for i in range(len(x)):
        yield i

b=list(function("VARDAN"))
print(b)