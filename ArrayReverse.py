def reverse(n):
    lst = list(range(1, n + 1))
    left = 0
    right = n - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
Array = [6, 5, 4, 3, 2, 1]
print(" Original Array : " + str(Array))
print(" Reversed Array : " + str(reverse(6)))