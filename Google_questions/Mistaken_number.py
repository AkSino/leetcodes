def palindrome(n):
    num=n
    rev=0
    while num>0:
        dig=num%10
        rev=rev*10 + dig
        num=num//10
    if rev==n:
        return True
    else:
        return False


def findMistaken(n):
    mistaken=0
    if n<11:
        return 0
    for i in range(12,n+1):
        if i%10!=0 and palindrome(i)==False:
            mistaken+=1

    return mistaken


print(findMistaken(50))



