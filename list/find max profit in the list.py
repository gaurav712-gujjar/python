prices=[10,60,40]
profit=0

for day in range(0,len(prices)-1):
    buy_price=prices[day]
    print(day,prices[day])

    for nextday in range( day+1 ,len(prices)):
        sell_price=prices[nextday]

        if(sell_price - buy_price > profit):
            profit=sell_price - buy_price

print(profit)