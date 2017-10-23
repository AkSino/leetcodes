#https://www.careercup.com/question?id=5753739085348864


Array=[1,2,44,56,98,99]
str=""
if len(Array)==0:
    print("0-99")
if Array[0]-0>0:
    if Array[0]-0==1:
        str=str + "0,"
    if Array[0]-0>1:
        str = str + ("%d-%d," % (0, Array[0]- 1))
for i in range(len(Array)-1):
    if Array[i+1]-Array[i]==2:
        str=str + ("%d," %Array[i]+1)
    if Array[i+1] - Array[i] > 2:
        str=str + ("%d-%d,"%(Array[i]+1,Array[i+1]-1))
if 99-Array[-1]>0:
    if 99-Array[-1]== 1:
        str = str + "99"
    if 99 - Array[-1] > 1:
        str = str + ("%d-%d" % (Array[-1]+1, 99))
if str[-1]==",":
    print(str[:-1])
else:
    print(str)
