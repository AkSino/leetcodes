amount=8
coins=[2,4,5]
number_of_coins=len(coins)
arr=[[] for x in range(amount+1)]

for coin_selected in coins:
    for current_array_number in range(1,amount+1):
        if coin_selected==current_array_number:
            arr[current_array_number].append([coin_selected])

        if coin_selected<current_array_number:
            remainder=current_array_number/coin_selected
            round_rem=int(remainder)
            if(remainder==round_rem):
                for each_element in arr[round_rem]:
                    arr[current_array_number].append(each_element+[coin_selected])

print(arr[amount])