deposit = 1000
profit_rate = 0.07
profit_duration = 0
while (profit_duration < 7):     
    daily_profit = deposit * 0.07
    deposit += daily_profit
    profit_duration = profit_duration + 1
print(deposit)
