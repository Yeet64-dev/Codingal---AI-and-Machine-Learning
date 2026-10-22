def move_zeros(n):
    bin = [0,1] * n
    return [x for x in bin if x == 1] + [0] * bin.count(0)
input("move_zeros(n) moves all zeros to the end of [0,1,0,1,...].  Press Enter")
print("  move_zeros(3) = [1, 1, 1, 0, 0, 0]")
print("  move_zeros(4) = [1, 1, 1, 1, 0, 0, 0, 0]")
n = int(input("Enter n (try 5 or 6): "))
guess = input("What is move_zeros(" + str(n) + ")? ")
input("write pointer collects non-zeros -- fill the rest with zeros.  Press Enter")
print("  move_zeros(" + str(n) + ") =", move_zeros(n), "  your guess:", guess)