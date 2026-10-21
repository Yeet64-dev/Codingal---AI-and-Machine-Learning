def max_profit(n):
    prices = list(range(n, 0, -1)) + list(range(1, n + 1))
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
input("max_profit(n) finds the best single buy-sell in prices [n..1, 1..n].  Press Enter")
print("  max_profit(4) = 3")
print("  max_profit(5) = 4")
n = int(input("Enter n (try 6 or 7): "))
guess = int(input("What is max_profit(" + str(n) + ")? "))
input("track min price so far -- sell when the gap beats the current best.  Press Enter")
print("  max_profit(" + str(n) + ") =", max_profit(n), "  your guess:", guess)