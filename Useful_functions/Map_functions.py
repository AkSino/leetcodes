import math
import collections
var=[1,2,3,4]
x = list(map(lambda x: x**2, var))
print(x)
#map uses one methon and calls it with a iterable datatype like list.



#Lambda is simply a method of defining an anonymous function, mostly used in conjunction with map
var=[1,2,3,4]

x = (lambda xy: xy**2)
print(x(2))

reduce_list=list(map(lambda x:print(x),list(filter(lambda x:x==3,var))))


p=[1,2,3,4,5,6,7,8]
print(p[1::2])