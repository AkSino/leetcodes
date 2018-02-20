amount=11
coins=[2,4]
number_of_coins=len(coins)
arr=[[] for x in range(amount+1)]

for coin_selected in coins:
    for current_array_number in range(1,amount+1):
        if coin_selected==current_array_number:
            arr[current_array_number].append([current_array_number])
        if coin_selected<current_array_number:
            diff=current_array_number-coin_selected
            for ph in arr[diff]:
                arr[current_array_number].append(ph+[coin_selected])

min_len=10000000
for each in arr[amount]:
    if len(each)<min_len:
        answer=each
        min_len=len(each)
for
print(answer)

#Basically we will start from a single coin, and then find in how mny ways that particular coin can make number from (o to Number_we_want)
#Then we use another coin, and find how many ways are added if we use that coin
# So the basic concept is if we are taking 2 rupee coin, and want to make a number 5, then we see in how many ways 3 was made earlier
# with the two coins and add the number 2 two each combination of 3