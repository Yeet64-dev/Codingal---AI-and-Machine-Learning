
def max_ones(n):
    bin = [1] * n + [0] + [1] * n
    streak = 0
    best = 0
    for i in range(len(bin)):
        if bin[i] == 1:
            streak += 1
            best = max(best, streak)
        else:
            streak = 0
    return best
input("max_ones(n) finds the longest run of 1s in [1..1, 0, 1..1].  Press Enter")
print("  max_ones(3) = 3")
print("  max_ones(4) = 4")
n = int(input("Enter n (try 5 or 6): "))
guess = input("What is max_ones(" + str(n) + ")? ")
input("streak resets to 0 on each 0 -- best keeps the highest streak seen.  Press Enter")
print("  max_ones(" + str(n) + ") =", max_ones(n), "  your guess:", guess)
