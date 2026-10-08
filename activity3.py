def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)
input("paths(m, n) counts routes through an m x n grid moving only right or down.  Press Enter")
print("  paths(3,3) = 6")
print("  paths(4,4) = 20")
n = input("Enter grid size for both rows and cols (try 5 or 6): ")
guess = input("What is paths(" + n + ", " + n + ")? ")
input("each call branches into two — move down or move right — the tree grows fast.  Press Enter")
print("  paths(" + n + ", " + n + ") = " + str(paths(int(n), int(n))) + "  your guess: " + guess)