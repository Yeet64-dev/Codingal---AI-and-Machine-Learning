def win_sum(n):
    bin = [0]*n + [1]*n
    streak = best = bin[0]
    for x in bin[1:]:
        if streak < 0: streak = x
        else: streak = streak + x
        if streak > best: best = streak 
    return best

n = int(input("Enter n (try 5 or 6): "))
guess = int(input("What is win_sum(" + str(n) + ")? "))
print("  win_sum(" + str(n) + ") =", str(win_sum(n)), "  your guess:", guess)