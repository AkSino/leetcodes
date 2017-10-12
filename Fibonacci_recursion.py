def Fibonacci(number_of_digits):
    if number_of_digits==1:
        return 0
    if number_of_digits==2:
        return 1
    elif number_of_digits>2:
        return Fibonacci(number_of_digits-1)+Fibonacci(number_of_digits-2)
for i in range(10):
    print(Fibonacci(i))