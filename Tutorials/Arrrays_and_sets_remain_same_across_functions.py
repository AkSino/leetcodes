def vardan(a):
    a=[1,2,3]
    change(a)
    print(a)
def change(m):
    m[1]=4

n=[9,8,7]
vardan(n)
print(n)


y = [1,2,3]
z=list(y)
def plusOne(z):
    for x in range(len(z)):
        z[x] += 1
    return z

print (plusOne(z), y)


a = 2

def plusOne2(a):
    a += 1
    return a

print (plusOne2(a), a)