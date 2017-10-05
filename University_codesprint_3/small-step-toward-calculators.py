string=input().strip()
oper=None
if "+" in string:
    oper="plus"
elif "-" in string:
    oper="minus"

num1=None
num2=None

if oper=="plus":
    num1,num2=string.split("+")
    print(int(num1)+int(num2))
elif oper=="minus":
    num1,num2=string.split("-")
    print(int(num1)-int(num2))

