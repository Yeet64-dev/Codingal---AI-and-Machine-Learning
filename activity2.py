def count_paren(n):
    if n == 0:
        return 1
    else:
        total = 0
        for i in range(n):
            total += count_paren(i) * count_paren(n - 1 - i)
        return total

input("count_paren counts every valid {} sequence - returns 1 at each valid end. Press Enter")
print("  count_paren(1) = 1")
print("  count_paren(2) = 2")
n = int(input("Enter a number of pairs (try 3 or 4): "))
guess = input("What is count_paren(" + str(n) + ")? ")
input("l>r closes l<n opens - adds 1 at every valid ending. Press Enter")
print("  count_paren(" + str(n) + ") = " + str(count_paren(n)) + "  your guess: " + guess)