def count_combos(n):
    if not n:
        return 0
    return 3 ** len(n)
input("count_combos multiplies letter choices at each digit — 3 letters per step.  Press Enter")
print("  count_combos(2) = 3")
print("  count_combos(23) = 9")
n = input("Enter digits 2-9 (try '234' or '2345'): ")
guess = input("What is count_combos('" + n + "')? ")
input("count_combos = choices at digit 0  x  count_combos of the rest.  Press Enter")
print(" count_combos('" + n + "') = " + str(count_combos(n)) + "  your guess: " + guess)