def eq_mid(n):
    bin = [1]*n + [0] + [1]*n
    streak = 0
    best = 0
    for i in range(len(bin)):
        if bin[i] == 1:
            streak += 1
            best = max(best, streak)
        else:
            streak = 0
n = int(input("Enter n (try 5 or 6): "))
eq_mid = int(input("What is eq_mid(" + str(n) + ")? "))
print("  eq_mid(" + str(n) + ") =", eq_mid, "  your guess:", eq_mid)