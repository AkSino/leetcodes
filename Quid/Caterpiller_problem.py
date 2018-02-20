import itertools


def find_lcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm

def calling_lcm(array):

    num1 = array[0]
    num2 = array[1]
    lcm = find_lcm(num1, num2)

    for i in range(2, len(array)):
        lcm = find_lcm(lcm, array[i])

    return (lcm)
def countUneatenLeaves(n, a):
    dict={}
    i=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if a[j]>n or a[j]%a[i]==0:
                a.remove(a[j])
                j+=1
            else:
                j+=1
        i+=1
    pink=[]
    for L in range(1, len(a) + 1):
        for subset in itertools.combinations(a, L):
            pink.append(list(subset))
    count=n

    for each in pink:
        if len(each)==1:
            count-=n//each[0]
        elif len(each)%2==0:
            count+=n//calling_lcm(each)
        else:
            count-=n//calling_lcm(each)

    return (count)




(countUneatenLeaves(1000,[2,5,7,9]))



