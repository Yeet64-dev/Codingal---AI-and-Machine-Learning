def left_rotate(n):
    lst = [1, 2, 3, 4, 5]
    return lst[n:] + lst[:n]
input("left_rotate(n) shifts [1,2,3,4,5] left by n positions. Press Enter")
print("  left_rotate(1) = [2, 3, 4, 5, 1]")
print("  left_rotate(2) = [3, 4, 5, 1, 2]")
n = int(input("rotate by how many? (try 3 or 5):"))
guess = input("What is left_rotate(" + str(n) + ")? ")
input("slice from index n to end, then attach the first n elements. Press Enter")
print("  left_rotate(" + str(n) + ") =", left_rotate(n), "  your guess:", guess)