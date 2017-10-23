#https://leetcode.com/problems/nth-digit/description/
import time
def findNthDigit( n):
    start, size, step = 1, 1, 9
    while n > size * step:
        n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
    num=start + (n - 1) // size
    den=(n - 1) % size
    return int(str(num)[den])


print(findNthDigit(16))

