annual_price = int(input())

sneakers = annual_price - annual_price * 0.40
sportswear = sneakers - sneakers * 0.2
ball = sportswear * 0.25
other = ball * 0.2

expenses = annual_price + sneakers + sportswear + ball + other
print(expenses)