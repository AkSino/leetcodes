def FindCombinationWithoutRepetetion(num,arr,tot_nums,str,storeArray):
    if num<=0 :
        if storeArray!=0:
            print (storeArray)
        return
    for i in range(len(arr)):
        storeArray[tot_nums-num]=arr[i]
        FindCombinationWithoutRepetetion(num-1, arr,tot_nums,str,storeArray)


ls=[]
lens=5
arr=[1,2,3,5,0,"a","b"]
correction_string=[0 for i in range(len(arr))]

FindCombinationWithoutRepetetion(lens,arr,lens,ls,correction_string)