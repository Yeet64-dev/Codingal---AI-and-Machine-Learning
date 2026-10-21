def total_profit(n):
    return 2 * (n - 1)
input("total_profit(n) sums every upswing in prices [1, n, 1, n, 1].  Press Enter")
print("  total_profit(4) = 6")
print("  total_profit(5) = 8")
n = int(input("Enter n (try 6 or 7): "))
guess = int(input("What is total_profit(" + str(n) + ")? "))
input("add every positive step -- two peaks each contribute n-1.  Press Enter")
print("  total_profit(" + str(n) + ") =", total_profit(n), "  your guess:", guess)
