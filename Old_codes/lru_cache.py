from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(num):
    if num==1:
        return 1
    if num==2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

for i in range(1,50222200):
    print(fibonacci(i))