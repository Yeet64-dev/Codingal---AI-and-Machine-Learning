def ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return ways(n-1) + ways(n-2)
input("ways counts every distinct way to climb n stairs.  Press Enter ")
print("  ways(3) = 3")
print("  ways(4) = 5")
n = int(input("Enter a number of stairs (try 5 or 6): "))
guess = input("What is ways(" + str(n) + ")? ")
input("ways(stairs) = ways(stairs-1) + ways(stairs-2)  both branches always combine.  Press Enter ")
print("  ways(" + str(n) + ") = " + str(ways(n)) + "  your guess: " + guess)