import array as arr
# 1) Create a function to calculate the second largest element of a list:
def second_largest(lst):
    if len(lst) < 2:
        return None  # Not enough elements for a second largest
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

# 2) Create a sample list and find its size using `len()`.
sample_list = [1, 2, 3, 4, 5]
size = len(sample_list)

# 3) Call the function and print the second largest element.
second_largest_value = second_largest(sample_list)
print("Second Largest:", second_largest_value)