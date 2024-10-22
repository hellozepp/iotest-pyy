# Given values
total_buy_amount = 1553268.42
total_sell_amount = 1072977.9
share_price = 1.524
loss_amount = 480290

# Calculate total cost
total_cost = total_buy_amount - loss_amount

# Calculate number of shares sold
number_of_shares_sold = total_sell_amount / share_price

# Calculate total cost per share
total_cost_per_share = total_cost / number_of_shares_sold

print(f"卖出时的总成本每股股价为: {total_cost_per_share:.2f} 元")