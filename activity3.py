def rainwater(n):
    return n
input("rainwater(n) traps water between two bars of height n.  Press Enter")
print("  rainwater(3) = 3")
print("  rainwater(4) = 4")
n = int(input("Enter bar height (try 5 or 6): "))
guess = int(input("What is rainwater(" + str(n) + ")? "))
input("water = min(left tallest, right tallest) - bar height at the gap.  Press Enter")
print("  rainwater(" + str(n) + ") =", rainwater(n), "  your guess:", guess)