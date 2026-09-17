def sum_down(n):
    if n == 0:
        return 0
    else:
        return n + sum_down(n-1)
input("Recursion - a function calls itself until a base case stops it. Press Enter")
print("  sum_down(3) = 3 + 2 + 1 + 0 = 6")
print("  sum_down(4) = 4 + 3 + 2 + 1 + 0 = 10")
n = int(input("Enter a number (try 5 or 6): "))
guess = int(input("What is sum_down(" + str(n) + ")? "))
input("sum_down adds n to sum_down(n-1) until n is 0. Press Enter")
print("  sum_down(" + str(n) + ") = " + str(sum_down(n)))