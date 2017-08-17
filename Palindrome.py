num=int(input())
arr=[]
x=1
print(type(x))
while x>=1:
    x=int(num/10)
    arr.append(num%10)
    num=x
print(arr)
reverse_array=[]
for item in arr:
    reverse_array.append(item)
reverse_array.reverse()
print(reverse_array)

if reverse_array==arr:
    print("YES")
else:
    print("No, Its not a palindrome")