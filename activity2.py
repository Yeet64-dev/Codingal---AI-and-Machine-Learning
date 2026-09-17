def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
input("Factorial - n! = n x (n-1) x (n-2) x ... x 1  base case: 0! = 1. Press Enter")
print("  4! = 24  = 4 x 3 x 2 x 1")
print("  5! = 120 = 5 x 4 x 3 x 2 x 1")
n = int(input("Enter a number (try 5 or 6): "))
guess = int(input("What is " + str(n) + "! ? "))
input("n! = n x factorial(n-1) until n is 0. Press Enter")
print("  " + str(n) + "! = " + str(factorial(n)) + "  your guess: " + str(guess))