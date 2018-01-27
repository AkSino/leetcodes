a=9
b=6

if a<b:
    a,b=b,a

while b!=0:
    a=a%b
    a,b=b,a

print(a)