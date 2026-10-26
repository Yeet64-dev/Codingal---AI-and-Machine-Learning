def max_front(n):
    subarr = [-n] + [1]*n
    max_sum = 0
    for i in range(len(subarr)):
        for j in range(i, len(subarr)):
            current_sum = sum(subarr[i:j + 1])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

input("max_front(n) finds the max subarray sum in [1, 1, ..., 1, -1].  Press Enter")
print("  max_front(3) = 3")
print("  max_front(4) = 4")
n = int(input("Enter n (try 5 or 6): "))
guess = int(input("What is max_front(n): "))
input("best locks in n ones — the last -1 drags sum down but best holds.  Press Enter")
print("max_front(n) = ", max_front(n), "  your guess: ", guess,)
