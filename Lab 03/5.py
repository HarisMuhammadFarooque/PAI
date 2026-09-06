def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        
        elif price - min_price > profit:
            profit = price - min_price

    return profit

