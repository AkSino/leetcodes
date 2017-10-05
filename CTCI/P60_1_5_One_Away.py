arr1=['p','a','l','e']
arr2=['p','l','e']

arr1_len=len(arr1)
arr2_len=len(arr2)

if max(arr1_len,arr2_len)-min(arr1_len,arr2_len)>1:
    print("false")
if arr2_len==arr1_len:
    for char in arr1:
