def group_reverse(n):
    lst = [1, 2, 3, 4, 5, 6]
    return [lst[i:i+n][::-1] for i in range(0, len(lst), n)]
input("group_reverse(n) reverses [1,2,3,4,5,6] in chunks of n.  Press Enter")
print("  group_reverse(2) = [2, 1, 4, 3, 6, 5]")
print("  group_reverse(3) = [3, 2, 1, 6, 5, 4]")
n = int(input("Group size (try 1 or 6):"))
guess = input("What is group_reverse(" + str(n) + ")? ")
input("each chunk of n elements is flipped in place.  Press Enter")
print("  group_reverse(" + str(n) + ") =", group_reverse(n), "  your guess:", guess)