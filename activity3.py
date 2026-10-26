def max_after(n):
    subarr = [-n] + [1]*n
    current = best = subarr[0]
    for x in subarr[1:]:
        if current < 0: current = x
        else: current = current + x
        if current > best: best = current
    return best
input("max_after(n) finds the max subarray sum in [-n, 1, 1, ..., 1].  Press Enter")
print("  max_after(3) = 3")
print("  max_after(4) = 4")
n = int(input("Enter n (try 5 or 6): "))
guess = int(input("What is max_after(n): "))
input("big negative resets — then n ones add up to n.  Press Enter")
print("max_after(n) = ", max_after(n), "  your guess: ", guess,)