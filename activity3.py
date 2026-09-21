def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
input("Tree recursion - two recursive calls per step. press enter")
print("  fib(5) = 5  sequence: 0, 1, 1, 2, 3, 5")
print("  fib(6) = 8  sequence: 0, 1, 1, 2, 3, 5, 8")
n = int(input("Enter n (try 4 or 7): "))
guess = int(input("What is fib(" + str(n) + ")? "))
input("Fibonacci: fib(n) = fib(n-1) + fib(n-2). Press Enter")
print("  fib(" + str(n) + ") = " + str(fib(n)) + "  your guess: " + str(guess))