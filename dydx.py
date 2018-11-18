def arithmetic_boggle(magic_number, numbers):
    if(len(numbers)==0):
        if(magic_number==0):
            return True
        else:
            return False
    return helperFunction(magic_number - numbers[0], numbers, 1) or helperFunction(magic_number + numbers[0], numbers, 1)

def helperFunction(sum, array, index):
    if(index==len(array)):
        if(sum==0):
            return True
        else:
            return False
    return helperFunction(sum+array[index], array, index+1) or helperFunction(sum-array[index], array, index+1)


print(arithmetic_boggle(0, [42]))