deposited_sum = float(input())
deposit_length = int(input())
annual_rate = float(input())

price = deposited_sum + deposit_length * ((deposited_sum * (annual_rate / 100) ) / 12)
print (price)
