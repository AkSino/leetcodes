#Default dict is basically used so that we dont have to write that if x exist in dict then append else create a new key

from collections import defaultdict


a=defaultdict(list)
a[1].append(3)
a[1].append(3)
print(a)