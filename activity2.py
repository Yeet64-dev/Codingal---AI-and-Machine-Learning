import array as arr
# 1) Create a function to calculate the maximum of a list:
def maximum(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

# 2) Create a function to calculate the minimum of a list:
def minimum(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

# 3) Create a sample list and find its size using `len()`.
sample_list = [1, 2, 3, 4, 5]
size = len(sample_list)

# 4) Call both functions and print the maximum and minimum.
print("Maximum:", maximum(sample_list))
print("Minimum:", minimum(sample_list))