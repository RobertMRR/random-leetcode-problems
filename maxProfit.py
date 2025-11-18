# Best Time to Buy and Sell Stock
def maxProfit(prices):
    profit = 0
    buy_price = prices[0]
    for i in range(1, len(prices)):
        new_profit = prices[i] - buy_price
        if new_profit > profit:
            profit = new_profit
        if prices[i] < buy_price:
            buy_price = prices[i]
    return profit

print(maxProfit([10,1,5,6,7,1]))
print(maxProfit([10,8,7,5,2]))