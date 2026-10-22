buy_price = float(input("Enter the buy price: "))
sell_price = float(input("Enter the sell price: "))

if (sell_price > buy_price):
    profit = sell_price - buy_price
    print(f"You made a profit of ${profit}.")
elif (sell_price < buy_price):
    loss = buy_price - sell_price
    print(f"You incurred a loss of ${loss}.")