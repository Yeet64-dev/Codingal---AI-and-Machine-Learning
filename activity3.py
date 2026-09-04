input("XOR all - pairs cancel, two odd-occuring ones remain.  Press Enter ")
list = [1,4,3,3]
print(str(list), "  XOR of all: ", 1 ^ 4 ^ 3 ^ 3, "  1 and 4 are odd-occuring")
print("split bit ", 1, "  binary:", bin(1)[2:], "  4  binary:", bin(4)[2:])
n = input("Enter a number (try 6 or 9): ")
guess = input("Is bit 0 of " + str(n) + " ON? (yes/no): ")
print("Check the split bit. Press Enter ")
if (int(bin(int(n))[2:]) & 1):
    print(" ", n, "  binary:", bin(int(n))[2:], "  bit 0 is ON  your guess:", guess)
else:
    print(" ", n, "  binary:", bin(int(n))[2:], "  bit 0 is OFF  your guess:", guess)