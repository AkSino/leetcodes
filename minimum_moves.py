def method(arr1,arr2):
    ans=0
    for i in range(len(arr1)):
        a=str(arr1[i])
        b=str(arr2[i])
        for index in range(len(a)):
            if int(a[index])>int(b[index]):
                ans+=(int(a[index])-int(b[index]))
            else:
                ans+=(int(b[index])-int(a[index]))
    return ans


print(method([123,543],[321,279]))
