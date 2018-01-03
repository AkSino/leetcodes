# import random
# a=[i for i in range(1,101)]
# count=100
# while a:
#     p=input()
#     index=random.randint(0,count-1)
#     print(a[index])
#     a.pop(index)
#     count-=1
import tensorflow

var=tensorflow.variable("VARDAB")
sess=tensorflow.session()
sess.start(var)
