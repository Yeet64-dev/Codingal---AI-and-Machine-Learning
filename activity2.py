input("XOR all numbers - pairs cancel, the odd one remains.  Press Enter ")
list = [2, 3, 4, 3, 2]
print("list: ", list, "  3 appears twice, 2 appears twice, 4 appears once")
print("odd-occuring: ", 2 ^ 3 ^ 4 ^ 3 ^ 2)
n = input("Enter a number (try 7 or 11): ")
list = [3, 5, 3, 5, int(n)]
guess = input("which number in " + str(list) + " appears only once? (try to guess the answer): ")
print("You guessed: ", guess)
input("XOR cancels pairs - the odd one remains.  Press Enter ")
print("list: ", str(list), "   odd-occuring: ", 3 ^ 5 ^ 3 ^ 5 ^ int(n), " your guess: ", guess)