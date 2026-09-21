
def bounce(n):
    if n == 0:
        return 0
    rest = bounce(n - 1)
    return rest + 2 * n

input("Head recursion - recurse first  then add 2*n on the way back.  Press Enter ")
print("  bounce(3) =", bounce(3))
print("  bounce(4) =", bounce(4))

n = int(input("Enter a number (try 5 or 6): "))
guess = input("What is bounce(" + str(n) + ")? ")
input("bounce(n) = bounce(n-1) + 2*n  adds 2*n as it unwinds back up.  Press Enter ")
print("  bounce(" + str(n) + ") =", bounce(n), "  your guess:", guess)