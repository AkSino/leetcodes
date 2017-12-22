a=[1,2,3,4,5]
b=[2,4,1,5,6]

c=list(map(max,list(zip(a,b))))
print(c)


#It carries out its loop till the shorted length of iterable
a=[1,2]
b=[4,5,6,7]
c=list(map(max,list(zip(a,b))))
print(c)

a=[1,2]
b=[4,5,6,7]
z=list(zip(a,b))
print(z)
