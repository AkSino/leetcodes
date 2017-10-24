def FindCombinationWithoutRepetetion(num,arr,tot_nums,str,storeArray):
    if num<=0 :
        if storeArray[0]!=0:
            print (storeArray)
        return
    for i in range(len(arr)):
        storeArray[tot_nums-num]=arr[i]
        p=arr[0:i]+arr[i+1:len(arr)]
        FindCombinationWithoutRepetetion(num-1, p,tot_nums,str,storeArray)


ls=[]
lens=3
arr=[1,2,3,0]
correction_string=[0 for i in range(len(arr))]

FindCombinationWithoutRepetetion(lens,arr,lens,ls,correction_string)

