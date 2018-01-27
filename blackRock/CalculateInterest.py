import  math


down_payment=0
loan_amount=25000-down_payment
monthly_interest_rate=6
n=10
print((monthly_interest_rate/1200) * loan_amount )
print(1 - math.pow(1 + (monthly_interest_rate/1200),-n*12))
P = ((monthly_interest_rate/1200) * loan_amount ) / (1 - math.pow(1 + (monthly_interest_rate/1200),-n*12))

total_interest_for_loan=(P*n*12)-loan_amount
print((P))
print(round(total_interest_for_loan))