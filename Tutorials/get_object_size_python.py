import sys
a=2222222222
print(sys.getsizeof(a))

print(sys.getsizeof({'foosssssss': 'bar', 'baz': 'barssssss','foo': 'barsss','foo': 'bars','foo': 'barss','foo': 'bar'}))
print(sys.getsizeof([['foo', 'bar'], ['baz', 'bar'],['baz', 'bar'],['baz', 'bar'],['baz', 'bar']]))


#Even the empty dictionary takes the 240 byts of memory.
x={}
print(sys.getsizeof(x))