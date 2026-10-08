def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1
input("hanoi(n) counts the minimum moves to shift n disks from peg A to peg C.  Press Enter ")
print("  hanoi(1) = 1")
print("  hanoi(2) = 3")
n = int(input("Enter number of disks (try 3 or 4): "))
guess = input("What is hanoi(" + str(n) + ")? ")
input("hanoi(n) = 2 * hanoi(n-1) + 1  each disk moves twice plus the last disk.  Press Enter ")
print("  hanoi(" + str(n) + ") = " + str(hanoi(n)) + "  your guess: " + guess)