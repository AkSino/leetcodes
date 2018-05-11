word=[1,2,3,4]

numbers=1<<len(word)
print(numbers)


for i in range(numbers):
    for j in range(len(word)):
        if ((i>>j) & 1 )==1:
            print(word[j],end=",")
    print()
