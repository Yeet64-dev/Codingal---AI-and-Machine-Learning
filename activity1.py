def reverse(n):
    lst = list(range(1, n + 1))
    left = 0
    right = n - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

input("reverse(n) builds [1..n] and flips it end-to-end using two pointers. Press Enter")
print("  reverse(4) = [4, 3, 2, 1]")
print("  reverse(5) = [5, 4, 3, 2, 1]") 
n = int(input("Enter list size (try 6 or 7): "))
guess = input("What is reverse(" + str(n) + ")? ")
input("left and right swap and move inward until they meet in the middle. Press Enter")
print("  reverse(" + str(n) + ") =", reverse(n), "  your guess:", guess)
