def tail_recursion(n):
    if n == 0:
        return 0
    else:
        return tail_recursion(n-1) + n
input("Tail recursion - the last action is the recursive call. Press Enter")
print("tail_fact(4) = 24  = 4 x 3 x 2 x 1")
print("tail_fact(5) = 120 = 5 x 4 x 3 x 2 x 1")
n = int(input("Enter a number (try 3 or 6): "))
guess = int(input("What is tail_fact(" + str(n) + ")? "))
input("tail_fact multiplies n into acc at each step. Press Enter")
print("  tail_fact(" + str(n) + ") = " + str(tail_recursion(n)) + "  your guess: " + str(guess))