def max_mid(n):
    subarr = [-1,5,6,234,534,123, n,-3245,3425,213,523,-21,-1]
    max_mid = 0
    for i in range(len(subarr)):
        if subarr[i] > max_mid:
            max_mid = subarr[i]
    return max_mid

input("max_mid(n) finds the max subarray sum in [-1, n, -1].  Press Enter")
print("  max_mid(3) = 3")
print("  max_mid(4) = 4")
n = int(input("Enter n (try 5 or 6): "))
guess = int(input("What is max_mid(n): "))
input("negative at start resets — best locks in the peak value n.  Press Enter")
print("max_mid(n) = ", max_mid(n), "  your guess: ", guess,)