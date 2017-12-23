#the yield statement is used to define generators, replacing the return of a function to provide a result to its caller without
# destroying local variables. Unlike a function, where on each call it starts with new set of variables, a generator will resume
# the execution where it was left off.


#Generators are useful when we have something in millions
def square(arr):
    for i in arr:
        yield i*i

array=[1,2,3,4,5]
#not hold the entire result in memory. It yield one result at a time. This is waiting for us to ask for next result.

print(square(array))

#To ask for the next result we use the below syntax
print(next(square(array)))
print(next(square(array)))
print(next(square(array)))

#if we use like below
a=square(array)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

for i in a:
    print(i)

#other method of creating a generator

ans=(i*i for i in range(5))
print(ans)

for i in ans:
    print(i)
