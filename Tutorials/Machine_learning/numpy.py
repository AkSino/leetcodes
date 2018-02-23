import numpy as np


a=np.array([2,3,4,5,6,7,2,5,4,7,3,5,76,8,9])

print(a[False])

#Initially all the elements of numpy array can be considered to be True unless they get filled with manual False after passing through some conditions



#In normal array we cannot perform operation on integer and boolean together but in numpy we can do it as below. True will be considered as 1 and False
#will be considered as 0.
print(np.array([True, 1, 2]) + np.array([3, 4, False]))

#Accessing elements in numpy is same as normal array.
x = ["a", "b", "c"]
x[1]
np_x = np.array(x)
np_x[1]

#2D array in numpy
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

bb_np=np.array(baseball)
print(bb_np[bb_np>80])
print(bb_np.shape)