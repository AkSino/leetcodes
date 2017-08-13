number_of_test=int(input().strip())
hashs="#"
space=" "
number=number_of_test
number_hash=1
for i in range(number_of_test):
    print((number-1)*space,(number_hash*hashs),sep='')
    number-=1
    number_hash+=1





