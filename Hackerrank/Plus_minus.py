#https://www.hackerrank.com/challenges/plus-minus/problem
arr=[-4 ,3 ,-9 ,0 ,4, 1]
plus = 0
minus = 0
zero = 0
for each in arr:
    if each > 0:
        plus += 1
    elif each < 0:
        minus -= 1
    else:
        zero += 1
print("%.6f" % (plus / len(arr)))
print("%.6f" % (minus / len(arr)))
print("%.6f" % (zero / len(arr)))