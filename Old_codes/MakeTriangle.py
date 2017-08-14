number=int(input().strip())
hashs="#"
space=" "
number_hash=1
number_space=number-1
for i in range(number):
    print(number_space*space,number_hash*hashs,sep="")
    number_space-=1
    number_hash+=2