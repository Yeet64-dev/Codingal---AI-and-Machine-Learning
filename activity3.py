def max_zeros(n):
    bin = [1] + [0]*n + [1]
    streak = 0
    best = 0
    for i in range(len(bin)):
        if bin[i] == 0:
            streak += 1
            best = max(best, streak)
        else:
            streak = 0
    return best
input("max_zeros(n) finds the longest run of 0s in [1, 0..0, 1].  Press Enter")
print("  max_zeros(3) = 3")
print("  max_zeros(4) = 4")
n = int(input("Enter n (try 5 or 6): "))
guess = input("What is max_zeros(" + str(n) + ")? ")
input("streak resets to 0 on each 1 -- best keeps the highest streak seen.  Press Enter")
print("  max_zeros(" + str(n) + ") =", max_zeros(n), "  your guess:", guess)